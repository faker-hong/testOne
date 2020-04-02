import numpy as np
import pandas as pd
from IPython.display import display
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

try:
    data = pd.read_csv("./customers.csv")
    data.drop(['Region', 'Channel'], axis=1, inplace=True)
except:
    print("found error")

# TODO: Select three indices of your choice you wish to sample from the dataset
indices = ['Fresh', 'Milk', 'Grocery']

# Create a DataFrame of the chosen samples
samples = data[indices]
# samples = pd.DataFrame(data.loc[indices], columns=data.keys()).reset_index(drop=True)
print("Chosen samples of wholesale customers dataset:")
display(samples)

# 1.功能相关性，购买某一商品是否会购买一定其他商品

# TODO: Make a copy of the DataFrame, using the 'drop' function to drop the given feature
new_data = samples.drop(['Fresh', 'Milk'])

# TODO: Split the data into training and testing sets(0.25) using the given feature as the target
# Set a random state.
X_train, X_test, y_train, y_test = train_test_split(samples, new_data, random_state=1, test_size=0.25)

# TODO: Create a decision tree regressor and fit it to the training set
regressor = DecisionTreeRegressor()
regressor.fit(X_train, y_train)
predict = regressor.predict(X_test)

# TODO: Report the score of the prediction using the testing set
score = mean_squared_error(y_test, predict)

