class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp(i,j)为数组(i-1,j-1)之间的乘积
        # dp每一行的最大值
        # leetcode上超出时间限制
        # if len(nums) == 1:
        #     return nums[0]
        # n = len(nums)
        # max_num = 0
        # dp = [[1]*(n+1) for _ in range(n+1)]
        # for i in range(1, len(dp)):
        #     for j in range(i, len(dp)):
        #         dp[i][j] = dp[i][j-1]*nums[j-1]
        #         max_num = max(max_num, dp[i][j])
        #
        # return max_num
        import sys
        if len(nums) == 1:
            return nums[0]
        max_nums, imax, imin = -sys.maxsize, 1, 1
        for i in range(len(nums)):
            # 出现负数时就将最大最小值互换
            if nums[i] < 0:
                imax, imin = imin, imax
            imax = max(imax*nums[i], nums[i])
            imin = min(imin*nums[i], nums[i])
            max_nums = max(max_nums, imax)
        return max_nums


if __name__ == '__main__':
    s = Solution()
    nums = [2,3,-2,4]
    re = s.maxProduct(nums)
    print(re)