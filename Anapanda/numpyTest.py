import numpy as np
from  numpy.linalg  import *


def main():
    # list = [[1, 2], [3, 4]]
    # print(list)
    # np_list = np.array(list)
    # print(np_list.shape)  # 形状
    # print(np_list.size)  # 元素个数
    # print(np.zeros([4, 4]))  # 产生一个4 * 4的数组值为0
    # print("-----------随机数----------")
    print(np.random.rand(2, 2))
    # chice
    # print(np.random.choice([1, 2, 3, 4, 5]))    # 在已有的数据中随机挑选一个
    lst1 = np.array([1, 2])
    lst2 = np.array([3, 4])
    lst3 = lst1 + lst2
    print(lst3)                 # numpy中array不会合并两个数组，而是直接进行运算，+-*/都一样
    print(np.concatenate((lst1, lst2)))     # 合并用这个函数
    print(np.split(lst3, 2))                # 分割


if __name__ == '__main__':
    main()
