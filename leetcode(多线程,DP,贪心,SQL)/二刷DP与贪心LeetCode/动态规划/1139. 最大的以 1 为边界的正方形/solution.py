class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        # 最小正方形的边长
        res = 0

        # 点(i, j)的左边有连续多个个1， 和上边有连续多少个1
        l = [[0] * n for _ in range(m)]
        u = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                l[i][j] = u[i][j] = 1
                if i > 0:
                    u[i][j] += u[i-1][j]
                if j > 0:
                    l[i][j] += l[i][j-1]

                for k in range(min(u[i][j], l[i][j]), -1, -1):
                    if k > res and u[i][j-k+1] >= k and l[i-k+1][j] >=k:
                        res = k

        return res ** 2


if __name__ == '__main__':
    grid = [[1,1,0,0]]
    s = Solution()
    res = s.largest1BorderedSquare(grid)
    print(res)