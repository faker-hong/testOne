import pandas as pd
import numpy as np


# pandas 集成了matplotlib和numpy，可以直接点plot(X, Y, kind='选择图的种类')方法画图
# 1. 生成数据表
# ---导入
'''
    这里导入数据的时候可能发生问题的原因：
    1.文件格式并不是csv格式，只是单纯改了文件的后缀，引发读取出错
    2.保存文件编码格式并不是uft-8，只需要用文本打开，用utf-8编码格式保存即可
'''
# df = pd.DataFrame(pd.read_csv('./test.csv'))
# 如果存在列名，直接选择需要的列，如果不存在列名，会自动把第一行作为列名，可以用names自己添加列名
# df = pd.read_csv('', usecols = [])
# df = pd.read_csv('', names = [])

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
# dataframe属性
'''
    shape   形状
    index   行索引名
    columns 列名
    values  值
    T   行列转置
'''
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
# 索引拿数据
'''
    直接索引，先列后行。          data[列名][行名]
    按名字进行索引               data.loc[][]
    按数字索引，与数组取值一样    data.iloc[][]
    数字与名字混用                data.ix[][]
'''



# 3. 数据表清洗 ： 处理缺失值删除或者替换
'''
    处理NaN的数据
        1.判断数据中是否存在NaN
            pd.isnull(df)   这两个方法返回的是df，如果值不为NaN，返回True，反之False
            pd.notnull(df)
            这里可以利用numpy的any或者all判断
            np.all(pd.isnull(df))
        2.删除数据中的缺失值样本
            df.dropna(inplace=True)     为True会修改原来数据样本，False不会修改原来，返回新的df
        3.替换修改数据中的缺失值
            df.fillna(value, inplace=True)
        4.检查NaN数据是否全部处理完毕
            pd.notnull(df).all()
    如果碰到不是NaN的数据，有默认标记
        1.把默认值替换成NaN
            data_new = data.replace(to_replace="", value=np.nan)
        2.之后的操作就可以按NaN的方式处理了
'''
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
'''
    数据的离散化：举个性别的例子，字段性别，用1，2代表男女。离散化后为男，女两字段，用1，0代表是否为男或女
        1.分组
            自动分组sr =pd.qcut(data, bins)     数据，要分的组数
            自定义分组sr =pd.cut(data, [])       数据，分组的区间（区间的边界即可，例如身高[150, 160, 170, 180]）分三组
        2.将分组好的结果转换为one-hot编码
            pd.get_dummies(sr, prefix="")       series, 分组列名前缀
'''
# 数据表合并-----merge
'''
    numpy
        np.concatnate((data1, data2), axis=1)   合并数据， 合并方向
    pandas
        pd.concat([data1, data2], axis=1)
        pd.merge(left, right, how="", on=[])    左表，右表， 合并方式(left, right, inner, outer), 索引字段
'''
df1=pd.DataFrame({
    "id": [i for i in range(1, 6)],
    "gender": ['male', 'female', 'male', 'female', 'male'],
    "pay": ['Y', 'N', 'Y', 'Y', 'N'],
    "m-point": [12, 10, 20, 40, 40],
    "price": [12, 13, 14, 15, 16]}
)
# df_inner = pd.merge(df, df1, how='inner')   # 交集
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
# 数据排序,多字段排序，list填入排序列名，False为降序，默认为True，升序
# df.sort_values(by=列名, ascending=False)

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
'''
    交叉表与透视表：探寻两个字段之间的关系
        pd.corsstab(value1, value2)     两个字段
        df.pivot_table([], index=[])
'''
# 对gender列进行计数汇总    ----分组与聚合
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
# 前10条某些列的数据添加，index为False为不要行索引，有mode参数，是追加还是写入.
# header为False时重复追加不要header列名,columns为要储存的列名，对应不上列名会报错
# df1[:10].to_csv('df1.csv', columns=['id', 'gender', 'pay'], index=False, header=True, mode='a')

# 写入到Excle
# df1.to_excel('df1.xlsx', sheet_name='test_hc')

# 读取HDF5文件,二进制文件    储存支持压缩，减少磁盘利用率
# hdf5是存储三维数据的文件
# 这里个人理解是，多个dataframe数据，一个dataframe对应一个key，在读取的时候，填入对应的key，读取对应的dataframe
# dataframe.to_hdf("文件名", key="")
# pd.read_hdf('路径', key="")


# 读取json文件
# 参数lines,以行为样本,一条数据一行
# pd.read_json('路径', orient='records', lines='')
# dataframe.to_json('路径', orient='records', lines='')