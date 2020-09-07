from collections import defaultdict

user_dict = {}
users = ["faker1", "faker2", "faker3", "faker1", "faker3", "faker3"]
for user in users:
    if user not in user_dict:
        user_dict[user] = 1
    else:
        user_dict[user] += 1

# def gen_default():
#     return {
#         "name": "",
#         "age": 12
#     }
# default_dicts = defaultdict(gen_default)  # 初始化
# default_dicts['faker']
# print(default_dicts)

default_dict = defaultdict(int)   # 传入的参数是个对象名称  如：list

for user in users:
    default_dict[user] += 1

print(default_dict)