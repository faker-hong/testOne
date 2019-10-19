import pandas as pd
import numpy as np


# 1. 生成数据表
'''
    这里导入数据的时候可能发生问题的原因：
    1.文件格式并不是csv格式，只是单纯改了文件的后缀，引发读取出错
    2.保存文件编码格式并不是uft-8，只需要用文本打开，用utf-8编码格式保存即可
'''
# ---导入
# df = pd.DataFrame(pd.read_csv('./test.csv'))
# 这里可能发生的问题： 检查编译器中是否有xlrd库
# df = pd.DataFrame(pd.read_excel('./test_xlsx.xlsx'))
# ---用pandas创建
df = pd.DataFrame({
    'id': [i for i in range(1, 6)],
    'date': pd.date_range('20191018', periods=5),
    'name': ['faker', ' clear', '777 ', '', 'link'],
    'age': [22, 23, 24, 25, 26],
    'price': [10, np.nan, 12, 15, None]},
    columns=['id', 'date', 'name', 'age', 'price'])



# 2. 数据表信息的查看
# 查看维度
# df.shape
# 数据表基本信息(维度， 列名称， 数据格式， 所占空间等)
# df.info()
# 数据表的值
# df.values
# 数据表的列名
# df.columns
# 查看某一列的唯一值
# df['id'].unique()
# 查看各列空值的数量
# df.isnull().sum()
# 查看数据
# df.head()   前十条数据，默认位10
# df.tail()   后十条数据，默认为10



# 3. 数据表清洗
# 对NaN的值填充为0，但这里并没有对元数据进行更改
# print(df.fillna(value=0))
# 将price列填充为price的平均值，只返回这一列
# print(df['price'].fillna(df['price'].mean()))
# 清除字符空格,并修改在原df中
# df['name']=df['name'].map(str.strip)
# 大小写转换
# df['name'] = df['name'].str.upper()
# 更改列名称,并不会改变原df，需要赋值修改
# df.rename(columns={'name': 'names'})
# 数据替换，也可以多项，但得一一对应，[a, b, c],[a, b, c]
# print(df.replace(22, 220))



# 4. 数据预处理
df1=pd.DataFrame({
    "id": [i for i in range(1, 6)],
    "gender": ['male', 'female', 'male', 'female', 'male'],
    "pay": ['Y', 'N', 'Y', 'Y', 'N'],
    "m-point": [12, 10, 20, 40, 40],
    "price": [12, 13, 14, 15, 16]}
)
# 数据表合并-----merge
df_inner = pd.merge(df, df1, how='inner')   # 交集
# df_left = pd.merge(df, df1, how='left')
# df_right = pd.merge(df, df1, how='right')
# df_outer = pd.merge(df, df1, how='outer')   # 并集

# append 匹配不上的用NaN替换，匹配不上的字段在原数据表中添加没有的字段
# result = df.append(df1)

# concat 个人感觉用法与append类似，可用于一次多个表合并
# 这里只是一个例子，没有实例df2， df3
# frames = [df1, df2, df3]
# result = pd.concat(frames)

# 按照特定列的值排序：这里对原数据没有影响
# print(df1.sort_values(by=['m-point']))

# 设置列索引： 这里将'pay'列设置为索引： 这里对原数据没有影响
# print(df1.set_index('pay'))

# 对gender列中修改所代表意思
# df1['gender'] = np.where(df1['gender'] == 'male', '男', '女')

# 使用iloc用位置区域提取数据
# df1.iloc[:3, :2]
# df1.iloc[[2, 3, 4], [1, 3]]   提取2,3,4行,1,3列数据

# 判断gender列是否为female
# df1.isin(['female'])
# 将符合的条件提取出来
# df1.loc[df1['gender'].isin(['female'])]



# 5. 数据筛选
# 使用  '与'  进行筛选, 第一个参数是筛选的条件，第二个参数是需要显示的列
# df1.loc[(df1['pay'] == 'Y') & (df1['m-point'] > 20), ['id', 'gender']]

# 使用  '或'  进行筛选
# df1.loc[(df1['pay'] == 'Y') | (df1['m-point'] > 20)]

# 使用  '非'  进行筛选
# df1.loc[df1['gender'] != 'male']

# 使用query函数进行筛选
# 这里查找'm-point'时报错，可能存在特殊字符的原因，暂未解决-------------------------------------------
# df1.query('id == [1, 2]')
# print(df1.query('m-point == [20, 40]'))

# 对筛选过的数据求和
# df1.query('id == [1, 2, 3]').price.sum()



# 6. 数据汇总   主要函数groupby和pivote_table
# 对gender列进行计数汇总
# df1.groupby('gender').count()

# 按gender对id字段进行计算
# print(df1.groupby('gender')['id'].count())

# 对gender分组，并计算price的sum和平均值
# df_inner.groupby('gender')['price'].agg([len, np.sum, np.mean])



# 7. 数据统计
# 简单的数据采样   随机取n条数据
# df1.sample(n=3)

# 手动设置采样权重
# weights = [0, 0, 0, 0, 0.5, 0.5]
# df_inner.sample(n=2, weights=weights)

# 两个字段相关性分析, 系数在-1到1之间，解近1为正相关，解近-1为负相关， 0为无关
# df1['m-point'].corr(df1['price'])

# 数据表的相关性分析
# df1.corr()



# 8. 数据输出
# 写入到CSV文件
# df1.to_csv('df1.csv')

# 写入到Excle
# df1.to_excel('df1.xlsx', sheet_name='test_hc')