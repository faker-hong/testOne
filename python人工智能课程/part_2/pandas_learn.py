import pandas as pd
import numpy as np

# Series
groceries = pd.Series(data=['10', '20', 'nice', 'bad'], index=['red', 'blue', 'yellow', 'white'])
print(groceries)
print("维度：", groceries.ndim)
print("索引名：", groceries.index)
print("值：", groceries.values)
print("形状：", groceries.shape)
print("数据数量：", groceries.size)
print("判断一个索引名是否在这个Series的index中：", 'banana' in groceries)


# Accessing and Deleting Elements in Pandas Series
groceries.loc[['red', 'yellow']]    # loc使用索引名映射
groceries.iloc[[1, 3]]              # iloc使用常规数组下标映射
groceries['red'] = 2
groceries.drop('red', inplace=True) # 要在原Series中改变，需要inplace=True，否则不会在原Series上删除


# Arithmetic Operations on Pandas Series
fruits = pd.Series(data=[10, 6, 3], index=['apples', 'oranges', 'bananas'])
print(fruits+2)     # 对Series的运算，与numpy一样
# np中对数组的func对Series一样有效
X = np.sqrt(fruits)
print(X)



# Creating Pandas DataFrames
items = {'Bob': pd.Series(data=[245, 25, 55], index=['bike', 'pants', 'watch']),
         'Alice': pd.Series(data=[40, 110, 500, 45], index=['book', 'glasses', 'bike', 'pants'])}
df = pd.DataFrame(items)
print(df)

# Accessing Elements in Pandas DataFrames
print("dataframes定位先列后行：", items['Bob']['bike'])
# 增加新列
df['faker'] = df['Bob'] + df['Alice']
print(df)
# 增加新列，数据只要第二位之后的数据
df['hong'] = df['faker'][1:]
print(df)
# 增加一列到具体的位置
df.insert(2, 'kk', [1, 2, 3, 4, 5])
print(df)

# 删除, axis=1为列，为0为行
df = df.drop(['kk', 'faker', 'hong'], axis=1)
print(df)


# Dealing with NaN
items2 = [{'bikes': 20, 'pants': 30, 'watches': 35, 'shirts': 15, 'shoes':8, 'suits':45},
{'watches': 10, 'glasses': 50, 'bikes': 15, 'pants':5, 'shirts': 2, 'shoes':5, 'suits':7},
{'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4, 'shoes':10}]

store_items = pd.DataFrame(items2, index = ['store 1', 'store 2', 'store 3'])

# 如果一个sum()表示每一列的NaN的数量，再一个sum表示全部NaN的数量
NaN_count = store_items.isnull().sum().sum()

# dropna, axis为0表示每条记录出现NaN则删除，为1则表示每列出现NaN则删除该列
store_items.dropna(axis=0)
store_items.dropna(axis=1)  # 若要再原df上改变，需要加上参数inplace=True

# fillna
store_items.fillna(0, inplace=True)
print(store_items)


# Loading Data into a Pandas DataFrame
dataset = pd.read_csv(csv_path)

# 获取数据的前几条或后几条, 默认为5
dataset.head()
dataset.tail()

# 每列数据的分析,也可以选择具体的某一列
dataset.describe()

# 对列1和列2分组，查看列3的平均值
dataset.groupby(['colunms1', 'colunms2'])['colunms3'].mean()