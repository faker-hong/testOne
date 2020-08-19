class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 思路：
        # 构成最大的质数然后copy + 粘贴
        dp = [0] * (n+1)
        for i in range(2, n+1):
            count = i
            for j in range(1, i):
                if i % j == 0:
                    count = min(dp[j] + i / j, count)
            dp[i] = count

        return dp[n]


if __name__ == '__main__':
    s = Solution()
    res = s.minSteps(21)
    print(res)