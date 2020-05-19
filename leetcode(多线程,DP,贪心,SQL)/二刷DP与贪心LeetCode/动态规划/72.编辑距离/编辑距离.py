'''
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
 

示例 1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2：

输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

动态规划：
    如果两个word的字母相同，则需要改变的次数与dp[i-1][j-1]位置需要改变的次数相同
    如果不同，则为dp[i-1][j-1], dp[i][j-1], dp[i-1][j]之中最小的，并且+1，为minDistance
'''


def minDistance(word1, word2):
    n1 = len(word1)
    n2 = len(word2)

    if n1*n2 == 0:
        return n1+n2

    dp = [[0]*(n1+1) for _ in range(n2+1)]

    for i in range(n1+1):
        dp[0][i] = i

    for i in range(n2+1):
        dp[i][0] = i

    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if word1[i-1] == word2[j-1]:
                dp[j][i] = dp[j-1][i-1]
            else:
                dp[j][i] = 1 + min(dp[j-1][i], dp[j][i-1], dp[j-1][i-1])

    return dp[-1][-1]


if __name__ == '__main__':
    word1 = "intention"
    word2 = "execution"

    res = minDistance(word1, word2)
    print(res)