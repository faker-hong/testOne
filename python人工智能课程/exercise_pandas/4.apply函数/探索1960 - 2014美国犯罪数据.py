import numpy as np
import pandas as pd

url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv"
data = pd.read_csv(url)

# 1.分析数据
info = data.info()

# 2.把Year列的类型改为datetime64
data['Year'] = pd.to_datetime(data['Year'], format('%Y'))

# 3.把Year列set成index
data.set_index(data.Year, drop=True, inplace=True)

# 4.删除Total列
# del data['Total']
data.drop('Total', axis=1, inplace=True)

# 5.merge.分组Year列，以10年为间隔，其他值相加即可，但是population要取10年末的值
# resample() 改变采样的频率
data.resample('10AS').sum()
population = data['population'].resample('10AS').max()
data['population'] = population

# 6.统计.美国最危险的十年是什么时候
# 数据出现最大值返回，0返回的是索引，1返回的是列
data.idxmax(0)
