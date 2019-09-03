import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from tqdm import tqdm
import random

DATADIR = 'D:\\testOne\\Anapanda\\PetImages'
CATEGORIES = ["Dog", "Cat"]
IMG_SIZE = 200
training_data = []


def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        class_num = CATEGORIES.index(category)
        i = 0
        for img in os.listdir(path):
            print(i)
            i += 1
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                training_data.append([new_array, class_num])
            except Exception as e:
                print(e)


create_training_data()
random.shuffle(training_data)

X = []
Y = []

for features, label in training_data:
    X.append(features)
    Y.append(label)

X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
# (24946, 200, 200, 1)
print(X.shape)

import pickle

# 序列化对象
pickle_out = open("X.pickle", "wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("Y.pickle", "wb")
pickle.dump(Y, pickle_out)
pickle_out.close()