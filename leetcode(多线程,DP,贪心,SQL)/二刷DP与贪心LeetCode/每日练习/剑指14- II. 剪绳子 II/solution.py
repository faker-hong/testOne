class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] * (n+1)

        for i in range(1, n+1):
            for j in range(1, i):
                dp[i] = max(
                    dp[i],
                    j * (i - j),
                    dp[j] * (i - j)
                )

        return dp[-1] % 1000000007


if __name__ == '__main__':
    s = Solution()
    res = s.cuttingRope(10)
    print(res)