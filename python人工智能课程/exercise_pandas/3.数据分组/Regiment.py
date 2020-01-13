import pandas as pd

raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
        'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
        'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'],
        'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}

# define DataFrame
data = pd.DataFrame(raw_data, columns=raw_data.keys())
# print(data)

# 1.What is the mean preTestScore from the regiment Nighthawks?
result = data[data['regiment'] == 'Nighthawks'].groupby("regiment").mean()
# print(result)

# 2.Present general statistics by company
result = data.groupby("company").describe()
# print(result)

# 3.What is the mean each company's preTestScore
result = data.groupby("company").mean()['preTestScore']
# print(result)

# 4.Present the mean preTestScores grouped by regiment and company
result = data.groupby(['regiment', 'company']).preTestScore.mean()
# print(result)

# 5. Present the mean preTestScores grouped by regiment and company without heirarchical indexing
'''
    stack()函数将行索引变为列索引
    unstack()反之
'''
result = data.groupby(['regiment', 'company']).preTestScore.mean().unstack()
a = data.groupby(['regiment', 'company']).preTestScore.mean()
# print(result)
# print("------------------")
# print(a)

# 6.Group the entire dataframe by regiment and company
result = data.groupby(['regiment', 'company']).mean()
# print(result)

# 7.What is the number of observations in each regiment and company
result = data.groupby(['regiment', 'company']).size()
# print(result)

# 8.Iterate over a group and print the name and the whole data from the regiment
for name, group in data.groupby('regiment'):
    print(name)
    print(group)