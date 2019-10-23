class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        temp = [0]*(n+2)
        temp[0], temp[-1] = 1, 1
        for i in range(1, n+1):
            temp[i] = nums[i-1]
        # 状态转移方程：
        # f（x, y）= temp[x-1]*temp[y+1]*num[k] + f(x,k-1) + f(k+1, y)  这里temp的第一位和最后一为都为1
        dp = [[0]*(n+2) for _ in range(n+2)]
        for k in range(1, n+1):
            for i in range(1, n-k+2):
                j = i+k-1
                for p in range(i, j+1):
                    dp[i][j] = max(dp[i][j], dp[i][p-1]+dp[p+1][j]+temp[i-1]*temp[p]*temp[j+1])

        return dp[1][n]


if __name__ == '__main__':
    s = Solution()
    nums = [3,1,5,8]
    re = s.maxCoins(nums)
    print(re)