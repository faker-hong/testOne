class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.map = {}

        if len(nums) == 0: return 0
        res = self.backtrack(nums, 0, S)
        return res

    def backtrack(self, nums, i, rest):
        if i == len(nums):
            if rest == 0:
                return 1
            return 0

        key = str(i) + ',' + str(rest)
        if key in self.map:
            return self.map[key]

        # 选择+号
        rest -= nums[i]
        add = self.backtrack(nums, i + 1, rest)
        rest += nums[i]

        # 选择-号
        rest += nums[i]
        sub = self.backtrack(nums, i + 1, rest)
        rest -= nums[i]

        result = add + sub
        self.map[key] = result

        return result


if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1]
    S = 3
    s = Solution()
    res = s.findTargetSumWays(nums, S)
    print(res)