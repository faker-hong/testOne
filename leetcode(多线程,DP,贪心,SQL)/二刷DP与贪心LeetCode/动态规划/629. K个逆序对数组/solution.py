class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        mod = 10**9 + 7

        # dp[i][k] 1-i之间k个逆序数
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        # base case
        for i in range(n+1):
            dp[i][0] = 1

        for i in range(2, n + 1):
            for j in range(1, k + 1):
                for p in range(max(j - i + 1, 0), j+1):
                    dp[i][j] += dp[i-1][p]

        return dp[n][k] % mod

    # optimizer
    '''
    dp[n][k-1] = dp[n-1][k-1]+dp[n-1][k-2]+dp[n-1][k-3]+dp[n-1][k-4]+…+dp[n-1][k-n]

    dp[n][k] = dp[n-1][k]+dp[n-1][k-1]+dp[n-1][k-2]+…+dp[n-1][k+1-n+1]+dp[n-1][k-n+1]

    两式相减得：
    dp[n][k] = dp[n][k-1]+dp[n-1][k]-dp[n-1][k-n]
    '''
    def kInversePairs_(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        mod = 10**9 + 7

        # dp[i][k] 1-i之间k个逆序数
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        # base case
        for i in range(n+1):
            dp[i][0] = 1

        for i in range(2, n + 1):
            for j in range(1, k + 1):
                if j >= i:
                    dp[i][j] = dp[i][j-1] + dp[i - 1][j] - dp[i - 1][j - i]
                    if dp[i][j] < 0:
                        dp[i][j] += mod
                else:
                    dp[i][j] = dp[i][j-1] + dp[i - 1][j] - 0

        return dp[n][k] % mod