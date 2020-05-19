class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        valid = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= valid:
                valid = i
        return valid == 0


if __name__ == '__main__':
    s = Solution()
    s.canJump([2,3,1,1,4])