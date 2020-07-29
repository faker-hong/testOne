'''
理解为2个背包，一个背包装+的数字，一个背包装-的数字
sum(A) - sum(B) = target
sum(A) = target + sum(B)
sum(A) + sum(A) = target + sum(B) + sum(A)
2 * sum(A) = target + sum(nums)

sum(A) = (target + sum(nums)) / 2
'''


class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if sum(nums) < S or (sum(nums) + S) % 2 == 1: return 0

        # 求出sum(A)
        s = sum(nums)
        P = (s + S) // 2

        # dp table
        dp = [0] * (P + 1)

        # base case
        dp[0] = 1

        for num in nums:
            for j in range(P, num - 1, -1):
                dp[j] += dp[j - num]

        return dp[P]


if __name__ == '__main__':
    nums = [0,0,0,0,0,0,0,0,1]
    S = 1
    s = Solution()
    res = s.findTargetSumWays(nums, S)
    print(res)