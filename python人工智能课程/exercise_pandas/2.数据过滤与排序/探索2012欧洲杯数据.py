import numpy as np
import pandas as pd

# url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv'
# data = pd.read_csv(url, sep=',')
# data.to_csv("./Euro_2012_stats_TEAM.csv")

data = pd.read_csv("./Euro_2012_stats_TEAM.csv")

# 1.查看Goal列
# print(data.Goals)

# 2.多少支队伍参加本次比赛
attend_teams = data.Team.value_counts().count()
# print(attend_teams)

# 3.查看数据集信息
# info = data.info()
# print(info)

# 4. View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline
discipline = data[['Team', 'Yellow Cards', 'Red Cards']]
# print(discipline)

# 5.Sort the teams by Red Cards, then to Yellow Cards
# discipline.sort_values(['Red Cards', 'Yellow Cards'], ascending=False, inplace=True)
# print(discipline)

# 6.计算平均黄牌数
avg_yellow_cards = data['Yellow Cards'].sum() / data.shape[0]
avg_yellow_cards = np.around(avg_yellow_cards)
# print(avg_yellow_cards)

# 7.找出进球数大于6的球队
teams = data[data['Goals'] > 6]
# print(teams)

# 8.找出球队名开头为G的球队
Teams_G = data[data['Team'].str.startswith('G')]
# print(Teams_G)

# 9.只取前七列数据
seven_columns = data.iloc[:, :7]
# print(seven_columns)

# 10.不要倒数第三列
except_last_three = data.drop(data.iloc[:, -3:-2], axis=1)
# print(except_last_three)

# 11.Present only the Shooting Accuracy from England, Italy and Russia
result = data[['Team', 'Shooting Accuracy']]
result = result[result.Team.isin(['England', 'Italy', 'Russia'])]
print(result)