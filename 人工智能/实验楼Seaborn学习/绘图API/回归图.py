import seaborn as sns
import matplotlib.pyplot as plt

# 回归图的绘制函数主要有：lmplot 和 regplot。

iris = sns.load_dataset('iris')

# regplot 绘制回归图时，只需要指定自变量和因变量即可，regplot 会自动完成线性回归拟合。
sns.regplot(x="sepal_length", y="sepal_width", data=iris)


# lmplot 同样是用于绘制回归图，但 lmplot 支持引入第三维度进行对比，例如我们设置 hue="species"。
sns.lmplot(x="sepal_length", y="sepal_width", hue="species", data=iris)