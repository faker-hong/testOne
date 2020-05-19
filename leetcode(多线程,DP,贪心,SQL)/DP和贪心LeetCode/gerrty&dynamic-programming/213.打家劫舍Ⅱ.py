class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = 0
        cur = 0
        pre1 = 0
        cur1 = 0
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)

        for i in range(len(nums)-1):
            temp = cur
            cur = max(pre+nums[i], cur)
            pre = temp
        for i in range(1, len(nums)):
            temp = cur1
            cur1 = max(pre1 + nums[i], cur1)
            pre1 = temp
        return max(cur, cur1)


if __name__ == '__main__':
    s = Solution()
    nums = [2, 3, 2]
    re = s.rob(nums)
    print(re)