class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        for i in nums2:
            nums1.append(i)
        len1 = len(nums1)
        print(nums1)
        self.quickSort(self, nums1, 0, len1 - 1)
        print(nums1)
        if len1 % 2 == 0:
            re = (nums1[(len1-1) // 2] + nums1[(len1-1) // 2+1]) / 2
            return re
        else:
            re = nums1[(len1-1) // 2]
            return re

    @staticmethod
    def quickSort(self, nums, start, end):
        i = start
        j = end
        if i > j:
            return
        temp = nums[i]
        while i < j:
            while (temp <= nums[j] and i < j):
                j -= 1
            while (temp >= nums[i] and i < j):
                i += 1
            if start < end:
                z = nums[i]
                y = nums[j]
                nums[i] = y
                nums[j] = z

        nums[start] = nums[i]
        nums[i] = temp
        self.quickSort(self, nums, start, j - 1)
        self.quickSort(self, nums, j + 1, end)
p = Solution()
count = p.findMedianSortedArrays([1,2],[3,4])
print(count)