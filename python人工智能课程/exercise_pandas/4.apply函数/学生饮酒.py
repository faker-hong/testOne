import numpy as np
import pandas as pd

csv_url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv'
data = pd.read_csv(csv_url)

# 1.只取school到guardian字段
school_guradian = data.loc[:, 'school':'guradian']

# 2.创建一个lambda函数把string都大写
upper = lambda x: x.capitalize()

# 3.Capitalize both Mjob and Fjob
data['Mjob'].apply(upper)
data['Fjob'].apply(upper)

# 4.打印末尾数据
data.tail()

# 5.merge.原数据还是小写，将原数据的Mjob，Fjob改为大写
data['Mjob'] = data['Mjob'].apply(upper)
data['Fjob'] = data['Fjob'].apply(upper)

# 6.统计.创建一个majority方法，返回boolean值到一个新列legal_drinker
def majority(x):
    if x > 17:
        return True
    else:
        return False

data['legal_drinker'] = data['age'].apply(majority)

# 7.可视化.把number都乘以10
def times10(x):
    if type(x) == int:
        return 10*x
    else:
        return x

# applymap(),作用于dataframe的每一个元素
data.applymap(times10)