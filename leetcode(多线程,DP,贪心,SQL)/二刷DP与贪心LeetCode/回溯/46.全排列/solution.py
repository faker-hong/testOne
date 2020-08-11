class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []

        def helper(p):
            if len(p) == n:
                res.append(p)
                return
            for num in nums:
                if num not in p:
                    helper(p + [num])

        helper([])
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.permute([1, 2, 3])
    print(res)