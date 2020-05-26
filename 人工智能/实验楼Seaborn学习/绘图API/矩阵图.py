import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 矩阵图中最常用的就只有 2 个，分别是：heatmap 和 clustermap。

# heatmap 主要用于绘制热力图。
sns.heatmap(np.random.rand(10, 10))