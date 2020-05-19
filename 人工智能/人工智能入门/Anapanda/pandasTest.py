import numpy as np
import pandas as pd
from pylab import *


def main():
    # data structure
    dates = pd.date_range("20170329", periods=10)   # 以这个日期格式为第一条，总共10条
    df = pd.DataFrame(np.random.randn(10, 5), index=dates, columns=list("ABCDE"))  # 10行五列，index索引，columns列名
    s1 = pd.Series(list(range(10, 20)), index=pd.date_range("20170329", periods=10))

    # print(df)

    # basic
    data_for_three = df.head(3)     # 取前三条数据
    data_for_end = df.tail(3)       # 取后三条数据
    print(df.sort_index(axis=1, ascending=False))   # axis = 1为对上边一列的index进行排序，为0为对左边一列index排序， False为降序
    df.describe()               # 数据的分析，最大值最小值等等

    # Select
    print(df["A"])
    print(df[:3])
    print(df["20170329":"20170401"])
    print(df.loc["20170329":"20170402", ["B", "D"]])        # 取索引段内，B，D列信息
    print(df.at[dates[0], "B"])                             # 取特定位置的信息
    print(df.iloc[1, 4])                                    # 1行4列数据


    print(df[df.B>0])                       # B列大于0
    print(df[df["E"].isin([1, 2])])         # E列的值为1或2

    # Set
    s1 = pd.Series(list(range(10, 20)), index=pd.date_range("20170329", periods=10))
    df["F"] = s1
    print(df)

    # Missing value
    df1 = df.reindex(index=dates[:4], columns=list("ABCD")+["E"])
    df1.loc[dates[0]:dates[1], "G"] = 1
    print(df1)
    print(df1.dropna())     # 把缺失值的行删除
    print(df1.fillna("2"))      # 把缺失值的位置填充为2

    # Concat 拼接
    pieces = [df[:3], df[-3:]]
    print(pd.concat(pieces))        # 把前三行和后三行数据进行拼接

    left = pd.DataFrame({"key": ["x", "y"], "value": [1, 2]})      # key，value各为一列
    right = pd.DataFrame({"key": ["x", "z"], "value": [3, 4]})
    print(pd.merge(left, right, on="key", how="left"))   # how类似于sql的连接，可以是outer，inner，right

    df3 = pd.DataFrame({"A": ["a", "b", "c", "b"], "B": list(i for i in range(4))})
    print(df3.groupby("A").sum())

    # 透视表
    df4 = pd.DataFrame({'A': ["one", "one", "two", "three"]*6,
                        'B': ['a', 'b', 'c']*8,
                        'C': ['faker', 'faker', 'faker', 'hong', 'hong', 'hong']*4,
                        'D': np.random.randn(24)})
    print(pd.pivot_table(df4, values="D", index=["A", "B"], columns=["C"]))


    # Time Series
    t_exam = pd.date_range("20190901", periods=1000, freq="S")     # 间隔为秒S


    # Graph
    ts = pd.Series(np.random.randn(1000), index=t_exam)
    ts = ts.cumsum()
    ts.plot()
    show()

    #File
    df6 = pd.read_csv("")
    df7 = pd.read_excel("", "")     # 第一个参数为路径，第二个为excel是sheet1还是其他

    # 存入
    df6 = pd.to_csv("")
    df7 = pd.to_excel("")


if __name__ == '__main__':
    main()