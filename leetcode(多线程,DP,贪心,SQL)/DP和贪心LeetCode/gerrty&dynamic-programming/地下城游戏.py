class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        # 自下而上
        if not dungeon:
            return 0
        n = len(dungeon)
        m = len(dungeon[0])
        dp = [[0]*m for _ in range(n)]
        dp[-1][-1] = max(1, 1-dungeon[-1][-1])
        # 如果为整数则为1，负数则为1-dungeon[-1][-1]
        # 初始化下边界
        for i in range(m-2, -1, -1):
            dp[-1][i] = max(dp[-1][i+1] - dungeon[-1][i], 1)
        # 初始化右边界
        for j in range(n-2, -1, -1):
            dp[j][-1] = max(dp[j+1][-1] - dungeon[j][-1], 1)

        # 取右边或下边的最小值做计算
        for a in range(n-2, -1, -1):
            for b in range(m-2, -1, -1):
                dp[a][b] = max(1, min(dp[a+1][b], dp[a][b+1]) - dungeon[a][b])
        return dp[0][0]


if __name__ == '__main__':
    s = Solution()
    dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
    re = s.calculateMinimumHP(dungeon)
    print(re)