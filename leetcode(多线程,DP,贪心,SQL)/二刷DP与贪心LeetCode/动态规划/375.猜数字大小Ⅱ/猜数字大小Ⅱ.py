'''
我们正在玩一个猜数游戏，游戏规则如下：

我从 1 到 n 之间选择一个数字，你来猜我选了哪个数字。

每次你猜错了，我都会告诉你，我选的数字比你的大了或者小了。

然而，当你猜了数字 x 并且猜错了的时候，你需要支付金额为 x 的现金。直到你猜到我选的数字，你才算赢得了这个游戏。

示例:

n = 10, 我选择了8.

第一轮: 你猜我选择的数字是5，我会告诉你，我的数字更大一些，然后你需要支付5块。
第二轮: 你猜是7，我告诉你，我的数字更大一些，你支付7块。
第三轮: 你猜是9，我告诉你，我的数字更小一些，你支付9块。

游戏结束。8 就是我选的数字。

你最终要支付 5 + 7 + 9 = 21 块钱。
给定 n ≥ 1，计算你至少需要拥有多少现金才能确保你能赢得这个游戏。
'''
import sys


def getMoneyAmount(n):
    dp = [[0 for _ in range(n+2)] for _ in range(n+2)]

    # 动态规划方程，我们在i-j中选择数字，如果选择k，则需要在剩下[i, k-1]和[k+1, j]中取较大值加上k，和dp[i][j]取较大值才是最少花费
    # dp[i][j] = min(dp[i][j], max(dp[i][k-1], dp[k+1][j]) + k)
    # 先要初始化dp, 如果只有一个数字，则0花费
    for i in range(n, 0, -1):
        for j in range(i, n+1):
            if i == j:
                dp[i][j] == 0
            else:
                dp[i][j] = sys.maxsize
                for k in range(i, j+1):
                    dp[i][j] = min(dp[i][j], max(dp[i][k-1], dp[k+1][j]) + k)

    return dp[1][n]


if __name__ == '__main__':
    n = 10
    res = getMoneyAmount(n)
    print(res)