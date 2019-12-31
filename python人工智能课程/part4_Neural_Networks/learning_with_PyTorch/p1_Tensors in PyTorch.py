import numpy as np
import torch

import helper


x = torch.rand(3, 2)
print(x)

y = torch.ones(x.size())
print(y)

z = x + y
print(z)
print(z[0])
print(z[:, 1:])

# 原始z不会改变
print(z.add(1))
# 原始z会改变
print(z.add_(1))
# 改变形状
print(z.resize_(2, 3))

# numpy与torch互相转换
a = np.random.rand(4,3)
b = torch.from_numpy(a)     # 从numpy转为torch
b.numpy()   # 转为numpy


# a,b都会进行操作后改变
b.mul_(2)
print(a)
print(b)