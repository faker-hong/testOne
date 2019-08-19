class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        len1 = len(s)
        len2 = len(t)
        dp = [[0]*(len1+1) for i in range(len2+1)]
        for i in range(len1+1):
            dp[0][i] = 1

        for i in range(1, len2+1):
            for j in range(1, len1+1):
                if s[j-1] == t[i-1]:
                    dp[i][j] = dp[i-1][j-1]+dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    S = "rabbbit"
    T = "rabbit"
    re = s.numDistinct(S, T)
    print(re)