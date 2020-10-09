class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(len(strs) + 1)]

        for i in range(1, len(strs) + 1):
            ones = strs[i-1].count('1')
            zeros = strs[i-1].count('0')
            for j in range(m + 1):
                for k in range(n + 1):
                    dp[i][j][k] = dp[i-1][j][k]
                    if j >= zeros and k >= ones and dp[i][j][k] < dp[i-1][j-zeros][k-ones] + 1:
                        dp[i][j][k] = dp[i-1][j-zeros][k-ones] + 1
        return dp[-1][-1][-1]

    def opt_findMaxForm(self, strs, m, n):
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')
            for i in range(m, zeros-1, -1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(1 + dp[i - zeros][j - ones], dp[i][j])

        return dp[m][n]


if __name__ == '__main__':
    strs = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3
    s = Solution()
    s.findMaxForm(strs, m, n)
    s.opt_findMaxForm(strs, m, n)