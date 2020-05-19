import xgboost as xgb
import numpy as np
import pickle as pk
import math
from sklearn.linear_model import LinearRegression

dtrain = xgb.DMatrix('../data/train.txt')
dtest = xgb.DMatrix('../data/valid.txt')

param = {'silent':1, 'objective':'count:poisson', 'booster':'gbtree', 'base_score':5, "eval_metric": 'rmse',\
        'eta':0.1, 'max_depth': 3, 'gamma':0}

watchlist  = [(dtest,'eval'), (dtrain,'train')]


num_round = 300

bst = xgb.train(param, dtrain, num_round, watchlist)

pred = bst.predict(dtest)
pred_train = bst.predict(dtrain)

#train log model
y = dtrain.get_label()
log_y = [math.log(x) for x in y]
log_dtrain = dtrain
log_dtrain.set_label(log_y)

y_test = dtest.get_label()
log_y_test = [math.log(x) for x in y_test]
log_dtest = dtest
log_dtest.set_label(log_y_test)

log_param = {'silent':1, 'objective':'count:poisson', 'booster':'gbtree', 'base_score':5, "eval_metric": 'rmse',\
        'eta':0.2, 'max_depth': 3, 'gamma':0}

log_watchlist  = [(log_dtest,'eval'), (log_dtrain,'train')]


log_num_round = 200
print("training log model")
log_bst = xgb.train(log_param, log_dtrain, log_num_round, log_watchlist)
log_pred_log = log_bst.predict(log_dtest)
log_pred = []
for i in log_pred_log:
    log_pred.append(math.pow(math.e, i))

log_pred_train_log = log_bst.predict(log_dtrain)
log_pred_train = []
for i in log_pred_train_log:
    log_pred_train.append(math.pow(math.e, i))

#train sqrt model
#y = dtrain.get_label()
sqrt_y = [math.sqrt(x) for x in y]
sqrt_dtrain = dtrain
sqrt_dtrain.set_label(sqrt_y)

#y_test = dtest.get_label()
sqrt_y_test = [math.sqrt(x) for x in y_test]
sqrt_dtest = dtest
sqrt_dtest.set_label(sqrt_y_test)

sqrt_param = {'silent':1, 'objective':'count:poisson', 'booster':'gbtree', 'base_score':5, "eval_metric": 'rmse',\
        'eta':0.1, 'max_depth': 3, 'gamma':0}

sqrt_watchlist = [(sqrt_dtest,'eval'), (sqrt_dtrain,'train')]

sqrt_num_round = 200

print("training sqrt model")
sqrt_bst = xgb.train(sqrt_param, sqrt_dtrain, sqrt_num_round, sqrt_watchlist)
sqrt_pred_sqrt = sqrt_bst.predict(sqrt_dtest)
sqrt_pred = []
for i in sqrt_pred_sqrt:
    sqrt_pred.append(i * i)

sqrt_pred_train_sqrt = sqrt_bst.predict(sqrt_dtrain)
sqrt_pred_train = []
for i in sqrt_pred_train_sqrt:
    sqrt_pred_train.append(i * i)

#train pow model
#y = dtrain.get_label()
pow_y = [math.pow(x, 2) for x in y]
pow_dtrain = dtrain
pow_dtrain.set_label(pow_y)

#y_test = dtest.get_label()
pow_y_test = [math.pow(x, 2) for x in y_test]
pow_dtest = dtest
pow_dtest.set_label(pow_y_test)

pow_param = {'silent':1, 'objective':'count:poisson', 'booster':'gbtree', 'base_score':5, "eval_metric": 'rmse',\
        'eta':0.1, 'max_depth': 3, 'gamma':0}
pow_watchlist = [(pow_dtest,'eval'), (pow_dtrain,'train')]
pow_num_round = 200

print("training pow model")
pow_bst = xgb.train(pow_param, pow_dtrain, pow_num_round, pow_watchlist)
pow_pred_pow = pow_bst.predict(pow_dtest)
pow_pred = []
for i in pow_pred_pow:
    pow_pred.append(math.sqrt(np.abs(i)))

pow_pred_train_pow = pow_bst.predict(pow_dtrain)
pow_pred_train = []
for i in pow_pred_train_pow:
    pow_pred_train.append(math.sqrt(np.abs(i)))

x_data = []
for linear, log, sqrt, pw in zip(pred_train, log_pred_train, sqrt_pred_train, pow_pred_train):
    x_data.append([linear, log, sqrt, pw])
x_data = np.array(x_data)
y_data = np.array(list(y))
clf = LinearRegression()
clf.fit(x_data, y_data)

test_x = []
for linear, log, sqrt, pw in zip(pred, log_pred, sqrt_pred, pow_pred):
    test_x.append([linear, log, sqrt, pw])
test_x = np.array(test_x)

final_pred_test = clf.predict(test_x)

rmse = 0.0
for t, p in zip(y_test, final_pred_test):
    rmse += (t - p) * (t - p)
rmse /= len(y_test)

rmse = math.sqrt(rmse)

print "rmse = ", rmse