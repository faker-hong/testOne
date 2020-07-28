class Solution(object):
    # 空间消耗和时间消耗都很大
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 要分割成两个等和的子集，说明数组的sum得是偶数
        if sum(nums) % 2 != 0 or len(nums) < 2:
            return False

        # 和0-1背包问题相似，往背包中塞num， 如果和等于sum/2， 那么返回True
        target = int(sum(nums) / 2)

        dp = [[0] * (target + 1) for _ in range(len(nums))]

        for i in range(1, len(nums)):
            for j in range(1, target + 1):
                # 如果物品值等于target，返回True
                if nums[i - 1] == target:
                    return True

                # 装不下
                if j - nums[i - 1] < 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    # 可以装下与装不下择优
                    dp[i][j] = max(nums[i - 1] + dp[i - 1][j - nums[i - 1]],
                                   dp[i - 1][j])

        return dp[-1][-1] == target

    # 对dp数组进行压缩成一维的
    def canpartition_(self, nums):

        if len(nums) < 2 or sum(nums) % 2 != 0:
            return False

        target = int(sum(nums) / 2)
        dp = [False] * (target + 1)
        dp[0] = True

        for i in range(0, len(nums)):
            for j in range(target, 0, -1):
                if j - nums[i] >= 0:
                    dp[j] = dp[j] or dp[j - nums[i]]

        return dp[-1]


if __name__ == '__main__':
    nums = [1, 5, 11, 5]
    s = Solution()
    res = s.canPartition(nums)
    res_ = s.canpartition_(nums)
    print(res)
    print(res_)