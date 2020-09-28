class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return

        n = len(nums)

        if n == 1:
            return nums[0]

        left = 0
        right = n - 1

        if nums[left] < nums[right]:
            return nums[left]

        while left < right:
            mid = left + (right - left) / 2

            if nums[mid] > nums[mid+1]:
                return nums[mid+1]

            if nums[mid-1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1

