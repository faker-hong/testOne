'''
给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。

一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

题目数据保证答案符合 32 位带符号整数范围。

示例 1：

输入：S = "rabbbit", T = "rabbit"
输出：3
解释：

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^

dp[i][j]的值为
S中[0-j]能构成T[0-i]多少次

动态方程：
如果字母相等会出现两种情况，如果'abab'和'ab',
要是b都选取末尾的，那就是dp[i-1][j-1],
要是S不取末尾的，那就是dp[i][j-1],两种情况需要相加，
则：dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

如果不相等：
则：dp[i][j] = dp[i][j-1]
'''


def numDistinct(s, t):
    len1 = len(s)
    len2 = len(t)
    dp = [[0] * (len1 + 1) for i in range(len2 + 1)]
    for i in range(len1 + 1):
        dp[0][i] = 1

    for i in range(1, len2 + 1):
        for j in range(1, len1 + 1):
            if s[j - 1] == t[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
            else:
                dp[i][j] = dp[i][j - 1]
    return dp[-1][-1]


if __name__ == '__main__':
    s = 'word'
    t = 'ab'
    times = numDistinct(s, t)
    print(times)