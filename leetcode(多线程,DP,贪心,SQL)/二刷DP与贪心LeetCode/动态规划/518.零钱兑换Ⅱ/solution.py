class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # 零钱的数量是无限的，是一个完全背包问题
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]

        # base case
        # 没有零钱，就无法凑出amount，为0； amount为0则可以用零钱凑出，为1
        for i in range(len(coins) + 1):
            dp[i][0] = 1

        # 比如要用金额2的金币凑出金额5， 我知道了凑出金额3的方法，拿凑出金额5的方法总数，就等于凑出金额3和凑出金额2的方法数的和
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if j - coins[i - 1] < 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    # 凑出2，3的和
                    dp[i][j] = dp[i - 1][j] + \
                               dp[i][j - coins[i - 1]]

        return dp[-1][-1]

    # 降维处理
    def change_(self, amount, coins):
        # dp table
        dp = [0] * (amount + 1)

        # base case
        dp[0] = 1

        # i 每循环一次，dp[j]就相当于二维的dp[i - 1][j]
        for i in range(len(coins)):
            for j in range(1, amount + 1):
                if j - coins[i] >= 0:
                    dp[j] = dp[j] + dp[j - coins[i]]

        return dp[-1]


if __name__ == '__main__':
    amount = 5
    coins = [1, 2, 5]
    s = Solution()
    res = s.change(amount, coins)
    res_ = s.change_(amount, coins)
    print(res)
    print(res_)