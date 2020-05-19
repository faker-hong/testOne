class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        add, i, res = 1, 0, 0

        # 当补足的数大于n就无法对1-n之间的数造成影响
        # 范围最大为1-n, add-add+n, n-add之间的数无法表示
        while add <= n:
            if i < len(nums) and nums[i] <= add:
                add += nums[i]
                i += 1
            else:
                res += 1
                add += add
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 5, 10]
    n = 20
    re = s.minPatches(nums, n)