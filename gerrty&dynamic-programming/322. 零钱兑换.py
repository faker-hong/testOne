class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 与单词分割的题目类似
        # i - coins[i]剩下的金额所需最少次数在dp中是否存在
        dp = [float("inf")]*(amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i-coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin]+1)

        return dp[-1] if dp[-1] != float("inf") else -1


if __name__ == '__main__':
    s = Solution()
    coins = [4, 7]
    amount = 13
    re = s.coinChange(coins, amount)
    print(re)