import numpy as np


"""
    n:物品个数
    v:包能装的体积
    w:表示物品重量的列表
    p:表示物品价值的列表
    
    dp的值为包内的物品价值
"""
def package(n, v, w, p):
    dp = np.zeros([n+1, v+1])

    for i in range(1, n+1):
        for j in range(1, v+1):
            if j < w[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + p[i])
    return dp


if __name__ == '__main__':
    n = 4
    v = 8
    w = [0, 2, 3, 4, 5]
    p = [0, 3, 4, 5, 6]
    dp = package(n, v, w, p)
    print(dp)