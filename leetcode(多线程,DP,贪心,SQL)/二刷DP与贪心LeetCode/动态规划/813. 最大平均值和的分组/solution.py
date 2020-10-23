class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        # dp[i][j]表示前i个数分成j份构成的最大平均值和
        dp = [[0] * K for _ in range(len(A))]

        for i in range(len(A)):
            for j in range(K+1):
                if j == 0:
                    dp[i][j] = sum(A[:i+1]) / (i+1)
                else:
                    if i < j:
                        break
                    for k in range(i):
                        # dp[i][j]可以由dp[k][j-1] + sum(A[k+1: i+1]) / (i-k)
                        dp[i][j] = max(dp[i][j], dp[k][j-1] + sum(A[k+1: i+1]) / (i-k))
        return dp[-1][-1]