class Solution(object):
    def minCostToMoveChips(self, chips):
        """
        :type chips: List[int]
        :rtype: int
        """
        '''
        数轴上放置了一些筹码，每个筹码的位置存在数组 chips 当中。

        你可以对 任何筹码 执行下面两种操作之一（不限操作次数，0 次也可以）：
        
        将第 i 个筹码向左或者右移动 2 个单位，代价为 0。
        将第 i 个筹码向左或者右移动 1 个单位，代价为 1。
        最开始的时候，同一位置上也可能放着两个或者更多的筹码。
        
        返回将所有筹码移动到同一位置（任意位置）上所需要的最小代价。
        
        '''
        odd = 0
        even = 0
        # 数组存的是筹码所在的位置，因为移动两步是不计数的，那就转换为0和1的位置问题了
        # 把偶数位置的筹码移到奇数位置，或者把奇数位置的筹码移到偶数位置，取较小值
        for i in chips:
            if i % 2 == 0:
                odd += 1
            else:
                even += 1
        return min(odd, even)


if __name__ == '__main__':
    S = Solution()
    chips = [1, 2, 3]
    result = S.minCostToMoveChips(chips)
    print(result)