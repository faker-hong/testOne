class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = nums[1] - nums[0]
        length = 0
        if pre == 0:
            length = 1
        else:
            length = 2
        for i in range(1, len(nums)):
            cur = nums[i] - nums[i-1]
            if (cur > 0 and pre <= 0) or (cur < 0 and pre >= 0):
                length += 1
                pre = cur
        return length


if __name__ == '__main__':
    s = Solution()
    re = s.wiggleMaxLength([1,2,3,3,3,3,3,3])
    print(re)