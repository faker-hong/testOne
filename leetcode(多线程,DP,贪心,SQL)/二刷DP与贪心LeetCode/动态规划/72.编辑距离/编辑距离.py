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


# 从两个字符串的最后一位开始匹配，如果相同都前进一步，如果不同，有增删改三种操作
# 这里是用DP table来解决重叠子问题
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


# 这里用递归方法来解决， 用备忘录来解决重叠子问题
def minDistance_(word1, word2):
    # 备忘录
    memo = dict()

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        # 如果i, j为0， 那剩下的编辑距离就为另一个字符串剩下的加上去
        if i == -1: return j + 1
        if j == -1: return i + 1

        if word1[i] == word2[j]:
            memo[(i, j)] = dp(i-1, j-1)     # 两个字符相同，什么也不用做
        else:
            memo[(i, j)] = min(
                dp(i - 1, j) + 1,         # 删除
                dp(i, j - 1) + 1,         # 增加
                dp(i - 1, j - 1) + 1      # 替换
            )

        return memo[(i, j)]

    return dp(len(word1) - 1, len(word2) - 1)


if __name__ == '__main__':
    word1 = "intention"
    word2 = "execution"

    res = minDistance(word1, word2)
    res_ = minDistance_(word1, word2)
    print(res)
    print(res_)