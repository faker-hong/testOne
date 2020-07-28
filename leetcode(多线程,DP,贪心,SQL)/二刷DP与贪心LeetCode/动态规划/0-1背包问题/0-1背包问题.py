'''
    0-1背包问题：
        W: 背包容量为w, int类型
        N：有n个物品， int类型
        wt: 类型为list， wt[i]第i个物品的重量
        val：类型为list， val[i]第i个物品的价值
'''


def knapsack(W, N, wt, val):
    # dp table
    # dp[n][w] 代表对于前n个物品，w容量最多能装下的总价值
    dp = [[0] * (W + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, W + 1):
            # 对于第i个物品，我们的选择是装下与不装下，因为索引是从1开始的，所以要减去1

            # 如果物品超过容量，装不下
            if j - wt[i - 1] < 0:
                dp[i][j] = dp[i - 1][j]
            else:
                # 物品可以装下, 但需要与装下的择优
                dp[i][j] = max(val[i - 1] + dp[i - 1][j - wt[i - 1]],
                               dp[i - 1][j])

    return dp[-1][-1]


if __name__ == '__main__':
    N = 3
    W = 4
    wt = [2, 1, 3]
    val = [4, 2, 3]
    res = knapsack(W, N, wt, val)
    print(res)