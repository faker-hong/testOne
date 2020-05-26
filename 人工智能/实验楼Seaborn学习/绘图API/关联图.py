import seaborn as sns
import matplotlib.pyplot as plt

# relplot 是 relational plots 的缩写，其可以用于呈现数据之后的关系，主要有散点图和条形图 2 种样式

iris = sns.load_dataset("iris")

# 对于不同的类别，看不出差别
sns.relplot(x="sepal_length", y="sepal_width", data=iris)

# 对于不同的类别进行着色
sns.relplot(x="sepal_length", y="sepal_width", hue="species", data=iris)

# style参数可以赋予不同类别的散点不同的形状
sns.relplot(x="sepal_length", y="sepal_width",
            hue="species", style="species", data=iris)

# 指定kind，支持线形图，这里是sepal_length与petal_length的线形图
sns.relplot(x="sepal_length", y="petal_length",
            hue="species", style="species", kind="line", data=iris)