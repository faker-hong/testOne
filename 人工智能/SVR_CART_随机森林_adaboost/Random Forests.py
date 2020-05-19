import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

wine = np.loadtxt("wine.data", delimiter=',')
x = wine[:, 1:]
y = wine[:, :1]

le = LabelEncoder()
y = le.fit_transform(y)
print("step1:divide dataSets")
train_features, test_features, train_targets, test_targets = train_test_split(x, y, random_state=True, train_size=0.6)

rf = RandomForestClassifier(n_estimators=1000, criterion='gini', max_features='sqrt',
                            max_depth=None, min_samples_split=2, bootstrap=True, n_jobs=1, random_state=1)
rf.fit(train_features, train_targets)
test_predict = rf.predict(test_features)
tree_test = accuracy_score(test_targets, test_predict)
print(tree_test)