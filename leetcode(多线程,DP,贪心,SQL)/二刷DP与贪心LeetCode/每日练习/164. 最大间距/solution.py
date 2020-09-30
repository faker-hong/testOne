class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0
        nums = sorted(nums)
        res = 0

        for i in range(1, n-1):
            res = max(res, nums[i] - nums[i-1])

        return res


if __name__ == '__main__':
    s = Solution()
    s.maximumGap([3,6,9,1])