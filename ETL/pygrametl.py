import datetime
import sys
import time

import psycopg2

# Depending on your system, you might have to do something like this
# where you append the path where pygrametl is installed
sys.path.append('/home/me/code')

import pygrametl
from pygrametl.datasources import CSVSource, MergeJoiningSource
from pygrametl.tables import CachedDimension, SnowflakedDimension, \
    SlowlyChangingDimension, BulkFactTable

# Connection to the target data warehouse:
pgconn = psycopg2.connect(user='me')
connection = pygrametl.ConnectionWrapper(pgconn)
connection.setasdefault()
connection.execute('set search_path to pygrametlexa')


# Methods
def pgcopybulkloader(name, atts, fieldsep, rowsep, nullval, filehandle):
    # Here we use driver-specific code to get fast bulk loading.
    # You can change this method if you use another driver or you can
    # use the FactTable or BatchFactTable classes (which don't require
    # use of driver-specifc code) instead of the BulkFactTable class.
    global connection
    curs = connection.cursor()
    curs.copy_from(file=filehandle, table=name, sep=fieldsep,
                   null=str(nullval), columns=atts)


def datehandling(row, namemapping):
    # This method is called from ensure(row) when the lookup of a date fails.
    # In the Real World, you would probably prefill the date dimension, but
    # we use this to illustrate "rowexpanders" that make it possible to
    # calculate derived attributes on demand (such that the - possibly
    # expensive - calculations only are done when needed and not for each
    # seen data row).
    #
    # Here, we calculate all date related fields and add them to the row.
    date = pygrametl.getvalue(row, 'date', namemapping)
    (year, month, day, hour, minute, second, weekday, dayinyear, dst) = \
        time.strptime(date, "%Y-%m-%d")
    (isoyear, isoweek, isoweekday) = \
        datetime.date(year, month, day).isocalendar()
    row['day'] = day
    row['month'] = month
    row['year'] = year
    row['week'] = isoweek
    row['weekyear'] = isoyear
    row['dateid'] = dayinyear + 366 * (year - 1990)  # Support dates from 1990
    return row


def extractdomaininfo(row):
    # Take the 'www.domain.org' part from 'http://www.domain.org/page.html'
    # We also the host name ('www') in the domain in this example.
    domaininfo = row['url'].split('/')[-2]
    row['domain'] = domaininfo
    # Take the top level which is the last part of the domain
    row['topleveldomain'] = domaininfo.split('.')[-1]


def extractserverinfo(row):
    # Find the server name from a string like "ServerName/Version"
    row['server'] = row['serverversion'].split('/')[0]


# Dimension and fact table objects
topleveldim = CachedDimension(
    name='topleveldomain',
    key='topleveldomainid',
    attributes=['topleveldomain'])

domaindim = CachedDimension(
    name='domain',
    key='domainid',
    attributes=['domain', 'topleveldomainid'],
    lookupatts=['domain'])

serverdim = CachedDimension(
    name='server',
    key='serverid',
    attributes=['server'])

serverversiondim = CachedDimension(
    name='serverversion',
    key='serverversionid',
    attributes=['serverversion', 'serverid'])

pagedim = SlowlyChangingDimension(
    name='page',
    key='pageid',
    attributes=['url', 'size', 'validfrom', 'validto', 'version',
                'domainid', 'serverversionid'],
    lookupatts=['url'],
    versionatt='version',
    fromatt='validfrom',
    toatt='validto',
    srcdateatt='lastmoddate',
    cachesize=-1)

pagesf = SnowflakedDimension(
    [(pagedim, (serverversiondim, domaindim)),
     (serverversiondim, serverdim),
     (domaindim, topleveldim)
     ])

testdim = CachedDimension(
    name='test',
    key='testid',
    attributes=['testname', 'testauthor'],
    lookupatts=['testname'],
    prefill=True,
    defaultidvalue=-1)

datedim = CachedDimension(
    name='date',
    key='dateid',
    attributes=['date', 'day', 'month', 'year', 'week', 'weekyear'],
    lookupatts=['date'],
    rowexpander=datehandling)

facttbl = BulkFactTable(
    name='testresults',
    keyrefs=['pageid', 'testid', 'dateid'],
    measures=['errors'],
    bulkloader=pgcopybulkloader,
    bulksize=5000000)

# Data sources - change the path if you have your files somewhere else
# The buffer size is set to 16384 B, as it performed better than any alternatives we tested
downloadlog = CSVSource(file('./DownloadLog.csv', 'r', 16384),
                        delimiter='\t')

testresults = CSVSource(file('./TestResults.csv', 'r', 16384),
                        delimiter='\t')

inputdata = MergeJoiningSource(downloadlog, 'localfile',
                               testresults, 'localfile')


def main():
    for row in inputdata:
        extractdomaininfo(row)
        extractserverinfo(row)
        row['size'] = pygrametl.getint(row['size'])  # Convert to an int
        # Add the data to the dimension tables and the fact table
        # 针对缓慢变化维度表使用的方法，如果没找到就添加
        row['pageid'] = pagesf.scdensure(row)
        # 查找给定的行，找不到就添加，返回键值，namemapping理解为row中的downloaddata对应维度表中的date属性
        # 如果查找失败，并且在创建时设置了rowexpander实列， 在执行插入之前调用rowexpander
        row['dateid'] = datedim.ensure(row, {'date': 'downloaddate'})
        # 查找，如果没找到添加默认值，找到直接添加
        row['testid'] = testdim.lookup(row, {'testname': 'test'})
        facttbl.insert(row)
    connection.commit()


if __name__ == '__main__':
    main()
