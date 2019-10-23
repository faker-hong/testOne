from collections import OrderedDict

user_dict = OrderedDict()
user_dict['b'] = "faker2"
user_dict['a'] = "faker1"
user_dict['c'] = "faker3"
print(user_dict)
print(user_dict.popitem())  # 删除末尾
print(user_dict.pop("a"))  # 必须要传入一个key的值
print(user_dict.move_to_end("b"))  # 也需要传入一个key
