class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)

        acc = [0] * (n + 1)
        for i in range(n):
            acc[i] = acc[i - 1] + nums[i]

        def merge(t1, t2):
            return t1[0] + t2[0], t1[1] + t2[1]

        from functools import lru_cache
        @lru_cache(None)
        def dp(i, m):
            if m == 0:
                return 0, []

            if n - i < m * k:
                return 0, []

            res_1 = dp(i + 1, m)
            res_2 = merge((acc[i + k - 1] - acc[i - 1], [i]), dp(i + k, m - 1))

            if res_1[0] > res_2[0]:
                return res_1
            return res_2

        return dp(0, 3)[1]


if __name__ == '__main__':
    s = Solution()
    s.maxSumOfThreeSubarrays([1, 2, 1, 2, 6, 7, 5, 1], 2)
