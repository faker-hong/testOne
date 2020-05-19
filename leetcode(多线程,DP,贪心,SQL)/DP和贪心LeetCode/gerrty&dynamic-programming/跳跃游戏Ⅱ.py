class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        times = 0
        maxlocation = 0
        locate = 0
        for i in range(0, len(nums)):
            maxlocation = max(maxlocation, nums[i]+i)
            if i == locate:
                locate = maxlocation
                times += 1
        return times


if __name__ == '__main__':
    s = Solution()
    print(s.jump([2,3,0,1,4]))