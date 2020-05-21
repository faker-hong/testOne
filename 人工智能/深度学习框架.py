import pandas as pd
from keras.callbacks import ModelCheckpoint
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense
from keras.models import Sequential
from sklearn.model_selection import train_test_split

# 第一步先获取数据，比如先读取到pandas的Dataframe
dataSets = pd.read_csv("")





# 第二步，数据处理，缺失值
isnull = dataSets.isnull().any()    # 返回的是每一列是否存在缺失值，boolean类型

# 对于缺失值的处理

# 1.删除
dataSets.dropna(axis=0, inplace=True)

# 2.用其他值填充,这里用列的均值填充每一列的缺失值
for column in list(dataSets.columns[dataSets.isnull().sum()>0]):
    mean_val = dataSets[column].mean()
    dataSets[column].fillna(mean_val, inplace=True)





# 第三步，特征工程
'''
1.如果存在最大最小值相差很大的数值型的列和最大最小值相差不大数值型的列，前者会对结果造成更大的影响
2.对于类别，等级的列，相同的道理

所以对于1情况，需要进行归一化或者标准化
对于情况2，需要进行ont-hot编码
'''
# 归一化(mean归一化，min-max归一化，也就是数值缩放到0-1，变换是线性的)或标准化(将数据变换为均值为0，方差为1的分布)
from sklearn.preprocessing import minmax_scale, StandardScaler


# 归一化，把数据映射到自定义范围内，避免某些特征max，min差别过大影响target，适用小数据
# 如果添加的数据max，min值出现异常的话，会影响target
def minmax_scale_demo():
    # 数据格式： 每年消耗公里数， 每年消耗冰淇淋重量， 每年出游时间占比，target
    data = pd.read_csv("")
    data = data.iloc[:, :3]
    # 实例转换器类, feature_range默认为[0, 1]
    transfer = minmax_scale(feature_range=[0, 1])
    data_new = transfer.fit_transform(data)
    print(data_new)


# 标准化, 不易受到异常点影响，适用大数据
'''
1、在分类、聚类算法中，需要使用距离来度量相似性的时候、或者使用PCA技术进行降维的时候，StandardScaler表现更好。

2、在不涉及距离度量、协方差计算、数据不符合正太分布的时候，可以使用MinMaxScaler。比如图像处理中，将RGB图像转换为灰度图像后将其值限定在[0 255]的范围。
'''
def StandardScaler_demo():
    # 数据格式： 每年消耗公里数， 每年消耗冰淇淋重量， 每年出游时间占比，target
    data = pd.read_csv("")
    data = data.iloc[:, :3]
    # 实例转换器类, 映射到-1到1
    transfer = StandardScaler()
    data_new = transfer.fit_transform(data)
    print(data_new)


# one-hot编码
# pandas自带get_dummies()方法
'''
data : array-like, Series, or DataFrame
输入的数据
prefix : string, list of strings, or dict of strings, default None
get_dummies转换后，列名的前缀
columns : list-like, default None
指定需要实现类别转换的列名
dummy_na : bool, default False
增加一列表示空缺值，如果False就忽略空缺值
drop_first : bool, default False
获得k中的k-1个类别值，去除第一个
'''
pd.get_dummies(dataSets, prefix=[], column=[], )






# 第四步，划分数据集(训练集，测试集，验证集)
x_train, x_test, y_train, y_test = train_test_split(dataSets[特征], dataSets[目标], random_state=True, test_size=0.2)







# 第五步，构建模型
'''
这是一个识别二维图片的model，包含卷积层，全连接层。
Flatten是从卷积层到全连接层，返回一个一维数组，因为全连接层需要一维的数据。
上一层的输出是下一层的输入，输出有10个类别，所以最后一层dense层输出为10

filter的个数为学习到的特征数，
padding的选择same和valid，same为不足kernel_size则舍去，valid则用其他值补足，一般为0
'''
model = Sequential()
model.add(Conv2D(filters=16, kernel_size=2, padding='same', activation='relu', input_shape=(32, 32, 3)))
model.add(MaxPooling2D(pool_size=2))
model.add(Conv2D(filters=32, kernel_size=2, padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=2))
model.add(Conv2D(filters=64, kernel_size=2, padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=2))
model.add(Dropout(0.3))
model.add(Flatten())
model.add(Dense(500, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(10, activation='softmax'))






# 第六步，训练
# 编译模型， 选择优化器和损失函数
model.compile(loss='categorical_crossentropy', optimizer='rmsprop',
              metrics=['accuracy'])

# 训练
checkpoint = ModelCheckpoint(filepath='model.weights.best.hdf5', verbose=1, save_best_only=True)

hist = model.fit(x_train, y_train, batch_size=32, epochs=100, validation_data=(x_valid, y_valid),
                 callbacks=[checkpoint], verbose=2, shuffle=True)

# 保存model
model.load_weights('model.weights.best.hdf5')

# 测试集准确率
score = model.evaluate(x_test, y_train, verbose=0)