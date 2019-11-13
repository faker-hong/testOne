import pymysql
import pygrametl
from pygrametl.tables import FactTable


conn = pymysql.Connect(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    db="etl_test",
    charset="utf8"
)

conn = pygrametl.ConnectionWrapper(connection=conn)

factTable = FactTable(
    name="facttable",
    measures=["sale"],
    keyrefs=["locationid", "bookid", "timeid"]
)

facts = [
        {'locationid': 1, 'bookid': 13, 'timeid': 4, 'sale': 50},
        {'locationid': 2, 'bookid': 7, 'timeid': 4, 'sale': 75},
        {'locationid': 1, 'bookid': 7, 'timeid': 4, 'sale': 50},
        {'locationid': 3, 'bookid': 9, 'timeid': 4, 'sale': 25}
]

for row in facts:
    factTable.insert(row)
conn.commit()


new_facts = [
        {'locationid': 1, 'bookid': 13, 'timeid': 4, 'price': 50},
        {'locationid': 2, 'bookid': 7, 'timeid': 4, 'price': 75},
        {'locationid': 1, 'bookid': 7, 'timeid': 4, 'price': 50},
        {'locationid': 3, 'bookid': 9, 'timeid': 4, 'price': 25}
]

# ensure等于lookup + insert方法
# ensure第二个参数设为True，除了键相同外，measures也需要相同，否则会报ValueError
for row in new_facts:
    factTable.ensure(row, True, {"sale": "price"})
conn.commit()
conn.close()