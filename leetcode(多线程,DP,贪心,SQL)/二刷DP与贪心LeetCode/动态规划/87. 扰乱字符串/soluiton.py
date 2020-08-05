import numpy as np
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n = len(s1)
        if n != len(s2):
            return False
        dp = [[[False] * (n + 1) for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                dp[i][j][1] = s1[i] == s2[j]
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                for j in range(n - l + 1):
                    for k in range(1, l):
                        if dp[i][j][k] and dp[i + k][j + k][l - k] or \
                                dp[i][j + l - k][k] and dp[i + k][j][l - k]:
                            dp[i][j][l] = True
                            break
        return dp[0][0][n]


if __name__ == '__main__':
    s1 = "great"
    s2 = "rgeat"
    s1 = "abcde"
    s2 = "caebd"
    s = Solution()
    res = s.isScramble(s1, s2)
    print(res)