'''
    对于峰值，有三种情况：
    1.数值呈递增状态，那右端为峰值
    2.数值呈递减状态，那左端为峰值
    3.峰值在中间

'''
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) / 2

            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid + 1

        return l