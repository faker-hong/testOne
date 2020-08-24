'''

思路分析： 使用动态规划法。dp[i][j]代表的是s[i, j]段打印的最少次数
状态转移方程：打印s[i, j]这段共有三种情况

第一种：dp[i][j] = 1 + dp[i + 1][j];//i单独打印， s[i + 1, j]段另外打印
第二种：dp[i][j] = min(dp[i][j], dp[i + 1][k] + dp[k + 1][j]);//dp[i + 1][k]代表将i放到[i+ 1, k]一起打印，dp[k + 1][j]代表[k + 1, j]另外打印，（s[i] == s[k])
第三种：dp[i][j] = min(dp[i][j], dp[i + 1][j]);//dp[i + 1][j]代表将i放入[j + 1, i]一起打印(s[i] == s[j])
'''


class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        n = len(s)
        dp = [[0] * (n+1) for _ in range(n+1)]

        # 第一次打印的长度
        for l in range(1, n+1):
            # 左端点
            for i in range(n-l+1):
                # 只打印左端点
                dp[i][i+l] = dp[i+1][i+l] + 1
                # 从左端点打印到k
                for k in range(i+1, i+l):
                    if s[k] == s[i]:
                        dp[i][i+l] = min(dp[i][i+l], dp[i][k] + dp[k+1][i+l])

        return dp[0][n]