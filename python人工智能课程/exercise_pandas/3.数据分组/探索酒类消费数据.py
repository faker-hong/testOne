import numpy as np
import pandas as pd

# drinks = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv')
# drinks.to_csv("./drinks.csv")

drinks = pd.read_csv("./drinks.csv")

# 1.Which continent drinks more beer on average?
result = drinks.groupby("continent").beer_servings.mean()
# print(result)

# 2.For each continent print the statistics for wine consumption
result = drinks.groupby("continent").wine_servings.describe()
# print(result)

# 3.Print the mean alcohol consumption per continent for every column
result = drinks.groupby("continent").mean()
# print(result)

# 4.apply函数.Print the median alcohol consumption per continent for every column
result = drinks.groupby("continent").median()
# print(result)

# 5.merge.Print the mean, min and max values for spirit consumption
result_1 = drinks.groupby("continent")["spirit_servings"].describe()
result_2 =drinks.groupby("continent").spirit_servings.agg(['mean', 'min', 'max'])
# print(result_1)
# print(result_2)