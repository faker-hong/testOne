from collections import ChainMap

user_dict1 = {"a": "faker1", "b": "faker2"}
user_dict2 = {"c": "faker3", "d": "faker4"}

"""
    如果要遍历这些dict，就需要一个个遍历，chainmap就解决了这个问题
    如果多个dict中存在相同的key，遍历中，后面重复的将不会被遍历
"""

new_dict = ChainMap(user_dict1, user_dict2)
# new_dict.new_child({"aa": "aa", "bb": "bb"})  # 不改变new_dict,而是返回一个新的dict
# print(new_dict)
print(new_dict.maps[0])  # 将合并的dict当成数组使用
for key, value in new_dict.items():
    print(key, value)