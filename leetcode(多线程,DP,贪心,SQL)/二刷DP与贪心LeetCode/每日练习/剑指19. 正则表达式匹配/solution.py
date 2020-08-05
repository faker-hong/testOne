class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # 增加一个相同字符，下面就不需要再-1
        s = '#' + s
        p = '#' + p

        for i in range(m + 1):
            for j in range(1, n + 1):
                # base case
                if i == 0:
                    if j > 1 and p[j] == '*':
                        dp[i][j] = dp[i][j - 2]
                # 能够直接匹配上或者模式串为'.'
                elif s[i] == p[j] or p[j] == '.':
                    dp[i][j] = dp[i-1][j-1]
                # 遇到*的情况
                elif p[j] == '*':
                    # *使用一次和不使用
                    if s[i] == p[j-1] or p[j-1] == '.':
                        # 前者为使用一次，后者为不使用
                        dp[i][j] = dp[i-1][j] or dp[i][j-2]
                    else:
                        dp[i][j] = dp[i][j-2]

        return dp[m][n]
