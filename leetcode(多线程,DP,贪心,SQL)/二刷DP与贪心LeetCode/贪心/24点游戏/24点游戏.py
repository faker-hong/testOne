from operator import truediv, mul, add, sub


class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        if len(nums) == 1:
            return abs(nums[0] - 24) < 1e-6

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    B = [nums[k] for k in range(len(nums)) if j != k != i]
                    for op in (truediv, mul, add, sub):
                        if (op is add or op is mul) and j > i: continue
                        if op is not truediv or nums[j]:
                            B.append(op(nums[i], nums[j]))
                            if self.judgePoint24(B):
                                return True
                            B.pop()

        return False


if __name__ == '__main__':
    solution = Solution()
    res = solution.judgePoint24([6, 6, 6, 6])
    print(res)