'''
示例 1:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出: true

示例 2:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出: false

'''


class Solution:
    def isInterleave(self, s1, s2, s3):
        '''
            字符串是否由s1和s2交错组成
        '''
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)

        if n1 + n2 != n3:
            return False

        dp = [[False] * (n2 + 1) for _ in range((n1 + 1))]

        dp[0][0] = True

        # 初始化第一行
        for i in range(1, n2 + 1):
            if dp[0][i - 1] and s2[i - 1] == s3[i - 1]:
                dp[0][i] = True

        # 初始化第一列
        for j in range(1, n1 + 1):
            if dp[j - 1][0] and s1[j - 1] == s3[j - 1]:
                dp[j][0] = True

        # dp
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                dp[i][j] = (dp[i][j - 1] and s2[j - 1] == s3[i + j -1]) or (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1])

        return dp[-1][-1]


if __name__ == '__main__':
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    s = Solution()
    res = s.isInterleave(s1, s2, s3)
    print(res)