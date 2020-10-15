'''
    用dic记录数字出现的次数：
    有三种情况：
        1.如果0出现3次及以上，那么存在一种[0, 0, 0]
        2.一个数x存在2次以上，如果有另一个数等于-2x, 那么存在一种[x, x, -2x]
        3.三个数从小到大为, x, y, z。 若x<0, 那么y+z = -x, z的最大值为数组中的最大值，最小值为y+z // 2,
        在x右侧找出y_z//2的下标z_id，便可得z的取值范围，即nums[z_id:]
        y的取值范围为大于x, y = y和z的和 - z


'''
import bisect
from collections import defaultdict


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dic = defaultdict(int)

        for i in nums:
            dic[i] += 1

        nums = sorted(dic)
        res = []

        for i, x, in enumerate(nums):
            if x == 0 and dic[x] > 2:
                res.append([0, 0, 0])
            elif x != 0 and dic[x] > 1:
                if -2*x in dic:
                    res.append([x, x, -2*x])

            if x < 0:
                y_z = -x
                z_id = bisect.bisect_right(nums, -x // 2, i+1)
                for z in nums[z_id:]:
                    y = y_z - z
                    if y > x and y in dic:
                        res.append([x, y, z])

        return res