import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
import matplotlib.pyplot as plt
import numpy as np
import pickle

from sklearn.model_selection import train_test_split

pickle_in = open("X.pickle", "rb")
X = pickle.load(pickle_in)

pickle_in = open("y.pickle", "rb")
y = pickle.load(pickle_in)

train_data, test_data, train_target, test_target = train_test_split(X, y, test_size=0.2, random_state=1)

train_data = train_data.reshape(train_data.shape[0], -1)
test_data = test_data.reshape(test_data.shape[0], -1)

cat_model = Sequential()
cat_model.add(Dense(512, activation='relu', input_shape=(40000,)))
cat_model.add(Dense(256, activation='relu'))
cat_model.add(Dense(128, activation='relu'))
cat_model.add(Dense(64, activation='relu'))
cat_model.add(Dense(1, activation='sigmoid'))   # 输出为一维的

cat_model.compile(optimizer=SGD(), loss='binary_crossentropy', metrics=['accuracy'])
cat_model.fit(train_data, train_target, epochs=5, batch_size=32)

print(cat_model.predict_classes(test_data))

# from skimage.transform import resize
#
# fig = plt.figure(figsize=(16, 16))
# for i in range(1, 10):
#     my_image = 'images/test/{}.jpg'.format(i)
#     my_image = np.array(plt.imread(my_image))
#     ax = fig.add_subplot(4, 5, i)
#     plt.imshow(my_image)
#     num_px = 64
#     my_image = resize(my_image, (num_px, num_px))
#     my_image.shape
#     my_image = my_image.reshape(1, -1)
#     a = cat_model.predict(my_image)
#     if a > 0.5:
#         ax.title.set_text('cat {}'.format(a))
#     else:
#         ax.title.set_text('dog {}'.format(1 - a))
#
# plt.show()
# cat_model.evaluate(x_test, y_test)