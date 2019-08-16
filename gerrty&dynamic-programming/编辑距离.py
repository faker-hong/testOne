class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)
        if m*n == 0:
            return m+n
        dp = [[0]*(m+1) for i in range(n+1)]

        for i in range(m+1):
            dp[0][i] = i
        for j in range(n+1):
            dp[j][0] = j
        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                # left = dp[i - 1][j] + 1
                # down = dp[i][j - 1] + 1
                # left_down = dp[i - 1][j - 1]
                # if word1[i - 1] != word2[j - 1]:
                #     left_down += 1
                # dp[i][j] = min(left, down, left_down)
        return dp[-1][-1]

if __name__ == '__main__':
    s= Solution()
    word1 = "horse"
    word2 = "ros"
    print(s.minDistance(word1, word2))