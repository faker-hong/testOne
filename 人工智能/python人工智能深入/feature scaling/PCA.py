import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import pandas as pd

iris = load_iris()

# 获取特征和目标值
X = iris.data
y = iris.target
# print(X)

pca = PCA(n_components=2)   # 保留两个特征
X_dec = pca.fit_transform(X)
X_dec.shape     # 这里就只有2个特征了


# 可视化
# 解释y == 0, 0    y值等于0的X_dec的第一列特征值，
# 那么y == 0, 1    y值等于0的X_dec的第二列特征值
plt.scatter(X_dec[y == 0, 0], X_dec[y == 0, 1], label=iris.target_names[0])
plt.scatter(X_dec[y == 1, 0], X_dec[y == 1, 1], label=iris.target_names[1])
plt.scatter(X_dec[y == 2, 0], X_dec[y == 2, 1], label=iris.target_names[2])
plt.title("PAC OF IRIS")
plt.legend()
plt.show()
