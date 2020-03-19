import pandas as pd


def get_train(url):
    train = pd.read_csv(url)
    train_target = train.loc[:, 'Score']
    train_features = train.iloc[:, 2:]
    return train_features, train_target


def get_test(url):
    test = pd.read_csv(url)
    test_target = test.loc[:, 'Score']
    test_features = test.iloc[:, 2:]
    return test_features, test_target