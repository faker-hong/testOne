class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        n = len(nums)
        res = []

        def helper(i, p):
            res.append(p)

            for j in range(i, n):
                helper(j + 1, p + [nums[j]])

        helper(0, [])
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.subsets([1, 2, 3])
    print(res)