class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        new = sorted(nums1 + nums2)
        n = len(new)

        median = n // 2
        if n % 2 == 0:
            return (new[median] + new[median - 1]) / 2.
        else:
            return new[median]

