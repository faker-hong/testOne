'''
有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

现在要求你戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。

求所能获得硬币的最大数量。

输入: [3,1,5,8]
输出: 167
解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
     coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

'''
# 状态转移方程：
# f（x, y）= temp[x-1]*temp[y+1]*num[k] + f(x,k-1) + f(k+1, y)  这里temp的第一位和最后一为都为1


def maxCoins(nums):
    nums = [1] + [i for i in nums if i > 0] + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

    for k in range(2, n):
        for left in range(0, n - k):
            right = left + k
            for i in range(left + 1, right):
                dp[left][right] = max(dp[left][right], nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
    return dp[0][n - 1]