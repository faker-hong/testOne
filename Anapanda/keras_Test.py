import numpy as np
from keras.models import Sequential     # 人工神经网络各个层的容器
from keras.layers import Dense, Activation      # Dense 神经层  Activation  激活函数
from keras.optimizers import SGD                # SGD 随机梯度下降算法
from sklearn.datasets import load_iris
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split

"""
五步法是用深度学习来解决问题的五个步骤： 

    1.构造网络模型 
    
    2.编译模型 
    
    3.训练模型 
    
    4.评估模型 
    
    5.使用模型进行预测
"""

def main():
    iris = load_iris()
    train_data, test_date, train_target, test_target = train_test_split(iris.data, iris.target, test_size=0.2, random_state=1)
    laber_train = LabelBinarizer().fit_transform(train_target)
    laber_test = LabelBinarizer().fit_transform(test_target)


    model = Sequential(
        [
            Dense(5, input_dim=4),  # input_dim为4对应的是鸢尾花的四个属性
            Activation("relu"),
            Dense(3, input_dim=5),  # 输入指的是上一层的输出   输出为3对应的是3个鸢尾花的种类
            Activation("sigmoid"),
        ]
    )
    # model = Sequential()
    # model.add(Dense(5, input_dim=4))    第二种方法添加

    sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)     # 优化器
    model.compile(optimizer=sgd, loss="categorical_crossentropy")   # 编译
    model.fit(train_data, laber_train, nb_epoch=200, batch_size=40)     # 训练数据，训练200轮，训练一次40个数据
    print(model.predict_classes(test_date))
    model.save_weights("./data/w")    # 模型比较大，训练时间长，可以把因子存下来，下次用

if __name__ == '__main__':
    main()