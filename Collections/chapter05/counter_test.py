from collections import Counter

# 作用与统计

users = ["faker1", "faker2", "faker3", "faker1", "faker3", "faker3"]
users_count = Counter(users)  # 传入的参数为可迭代的，字符串也是 可以的
print(users_count)

count_one = Counter("asjdasbdjkas")
count_two = Counter("aaaaa")
# count_one.update(count_two)
print(count_one)
print(count_one.most_common(2))  # top n 问题