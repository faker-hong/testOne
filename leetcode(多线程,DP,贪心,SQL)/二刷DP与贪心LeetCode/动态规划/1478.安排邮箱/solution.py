class Solution:
    def minDistance(self, houses, k):
        houses.sort()
        n = len(houses)

        # 一个邮箱需要的距离表
        cost = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                # 中位数
                mid = houses[(i + j) // 2]
                for l in range(i, j+1):
                    cost[i][j] += abs(mid - houses[l])      # 房屋在i-j之间的一个邮箱的最短距离和

        dp = [[float('inf')] * k for _ in range(n)]

        for i in range(n):
            for l in range(k):
                if l == 0:      # 一个邮箱所需的距离和与cost中的距离和相同
                    dp[i][l] = cost[0][i]
                elif l >= i:    # 如果邮箱数大于房屋数，那所需的距离和为0
                    dp[i][l] = 0
                else:
                    dp[i][l] = min(dp[k][l-1] + cost[l][k+1] for k in range(i))

        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    min_distance = s.minDistance([1, 2, 3, 4], 1)
    print(min_distance)