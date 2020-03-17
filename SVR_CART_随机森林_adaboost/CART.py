import numpy as np
from sklearn import tree
from sklearn.externals.six import StringIO
from sklearn.model_selection import train_test_split

print("step1:loading data")
wine = np.loadtxt("wine.data", delimiter=',')
x = wine[:, 1:]
y = wine[:, :1]
train_data, test_data, train_target, test_target = train_test_split(x, y, train_size=0.6, random_state=True)

print("step2:training")
clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

print("step3:testing")
predict = clf.predict(test_data)
right_number = 0
for i in range(len(test_target)):
    if predict[i] == test_target[i]:
        right_number += 1

accuracy = float(right_number/len(test_target))
print("accuracy=%.3f%%" % (accuracy*100))

