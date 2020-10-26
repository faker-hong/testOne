class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        nums.sort()
        dp = [[i] for i in nums]

        for i in range(len(nums)):
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j] == 0:
                    if len(dp[j]) + 1 > len(dp[i]):
                        dp[i] = dp[j] + [nums[i]]

        return max(dp, key=len)