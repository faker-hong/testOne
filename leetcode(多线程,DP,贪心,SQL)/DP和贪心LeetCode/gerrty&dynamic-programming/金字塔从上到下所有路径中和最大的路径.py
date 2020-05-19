import numpy as np


"""
    第一列的情况的，只能往正下方走，所以dp[i][j] = dp[i-1][j] + n[i][j]
    其他情况的话有两种走的选择，只要选择值最大就可以dp[i][j] = max(dp[i][i-1], dp[i-1][j-1]) + n[i][j]
    最后遍历一遍dp，选择最大值就是要的结果
"""
def longgst(n):
    dp = np.zeros([len(n), len(n)])
    dp[0][0] = n[0][0]
    res = 0
    for i in range(1, len(n)):
        for j in range(0, i+1):
            if j == 0:
                dp[i][j] = dp[i-1][j] + n[i][j]
            else:
                dp[i][j] = max(dp[i][i-1], dp[i-1][j-1]) + n[i][j]
            res = max(dp[i][j], res)
    return res


if __name__ == '__main__':
    n = [[3],
         [1,5],
         [8,4,3],
         [2,6,7,9],
         [6,2,3,5,1]]
    n = np.array(n)
    res = longgst(n)
    print(res)