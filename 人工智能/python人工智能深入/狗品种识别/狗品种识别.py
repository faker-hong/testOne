from sklearn.datasets import load_files
from keras.utils import np_utils
import numpy as np
import random
import cv2
from glob import glob
# glob模块是一个文件操作模块，返回所有匹配的文件路径的列表

# 定义函数来加载train，test和validation数据集
def load_dataset(path):
    data = load_files(path)
    dog_files = np.array(data['filenames'])
    dog_targets = np_utils.to_categorical(np.array(data['target']), 133)
    return dog_files, dog_targets

# 加载train，test和validation数据集
train_files, train_targets = load_dataset('dogImages/train')
valid_files, valid_targets = load_dataset('dogImages/valid')
test_files, test_targets = load_dataset('dogImages/test')

# 加载狗品种列表
dog_names = [item[20:-1] for item in sorted(glob("dogImages/train/*/"))]


# 导入人脸数据集
random.seed(8675309)

# 加载打乱后的人脸数据集的文件名
human_files = np.array(glob("lfw/*/*"))
random.shuffle(human_files)

# 提取预训练的人脸检测模型
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt.xml')

# 加载彩色（通道顺序为BGR）图像
img = cv2.imread(human_files[3])

# 将BGR图像进行灰度处理
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 在图像中找出脸
faces = face_cascade.detectMultiScale(gray)


# 如果监测到人脸返回True
def face_detector(path):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    return len(faces) > 0



'''
在使用 TensorFlow 作为后端的时候，在 Keras 中，CNN 的输入是一个4维数组(也被称作4维张量),它的各维度尺寸为 (nb_samples, rows, columns, channels)。
其中 nb_samples 表示图像（或者样本）的总数，rows, columns, 和 channels 分别表示图像的行数、列数和通道数。
'''

from keras.preprocessing import image
from tqdm import tqdm
# tqdm是一个快速，可扩展的进度条，在长循环中添加一个进度提示信息

def path_to_tensor(img_path):
    # 用PIL加载RGB图像为PIL.Image.Image类型
    img = image.load_img(img_path, target_size=(224, 224))
    # 将PIL.Image.Image类型转化为格式为(224, 224, 3)的3维张量
    x = image.img_to_array(img)
    # 将3维张量转化为格式为(1, 224, 224, 3)的4维张量并返回
    return np.expand_dims(x, axis=0)

def paths_to_tensor(img_paths):
    list_of_tensors = [path_to_tensor(img_path) for img_path in tqdm(img_paths)]
    return np.vstack(list_of_tensors)



# 定义自己的CNN
# 数据预处理，对图像进行归一化
from PIL import ImageFile
from keras.layers import Conv2D, MaxPooling2D, GlobalAveragePooling2D
from keras.layers import Dropout, Flatten, Dense
from keras.models import Sequential

ImageFile.LOAD_TRUNCATED_IMAGES = True

# keras中的数据预处理过程
train_tensors = paths_to_tensor(train_files).astype('float32')/255
valid_tensors = paths_to_tensor(valid_files).astype('fload32')/255
test_tensors = paths_to_tensor(test_files).astype('float32')/255

model = Sequential()

model.add(Conv2D(filters=16, kernel_size=2, strides=2, padding='valid', activation='relu', input_shape=()))
model.add(MaxPooling2D(pool_size=2))
model.add(Conv2D(filters=32, kernel_size=2, strides=2, padding='valid', activation='relu'))
model.add(MaxPooling2D(pool_size=2))
model.add(Conv2D(filters=32, kernel_size=2, strides=2, padding='valid', activation='relu'))
model.add(MaxPooling2D(pool_size=2))
model.add(GlobalAveragePooling2D())
model.add(Dropout(0.3))
model.add(Flatten())
model.add(Dense(133, activation='softmax'))

model.compile(metrics=['accuracy'], optimizer='rmsprop', loss='categorical_crossentropy')


# 训练模型
from keras.callbacks import ModelCheckpoint

epochs = 5

checkpoint = ModelCheckpoint(filepath='saved_models/weights.best.from_scratch.hdf5',
                             verbose=1,
                             save_best_only=True)
model.fit(train_tensors, train_targets,
          validation_data=(valid_tensors, valid_targets),
          epochs=epochs, batch_size=20, callbacks=[checkpoint], verbose=1)



## 加载具有最好验证loss的模型
model.load_weights('saved_models/weights.best.from_scratch.hdf5')


# 测试
