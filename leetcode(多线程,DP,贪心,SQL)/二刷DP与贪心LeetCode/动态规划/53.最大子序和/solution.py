import numpy as np
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp table dp[i]表示以nums[i]结果，构成的子数组最大和
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            # 选择加上，或者选择不加上
            dp[i] = max(nums[i], nums[i] + dp[i - 1])

        return max(dp)


if __name__ == '__main__':
    s = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    res = s.maxSubArray(nums)
    print(res)