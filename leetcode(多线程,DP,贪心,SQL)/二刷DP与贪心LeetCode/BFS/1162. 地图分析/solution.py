class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)

        # 找出所有的陆地位置，也就是1
        queue = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]
        distance = -1

        # 判断全是陆地或者全是海洋
        if len(queue) == 0 or len(queue) == n**2:
            return distance

        while len(queue) > 0:
            print(queue)
            for _ in range(len(queue)):
                x, y = queue.pop(0)
                for new_x, new_y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if 0 <= new_x < n and 0 <= new_y < n and grid[new_x][new_y] == 0:
                        queue.append((new_x, new_y))
                        grid[new_x][new_y] = -1
            distance += 1
        return distance


if __name__ == '__main__':
    s = Solution()
    s.maxDistance([[1,0,1],[0,0,0],[1,0,1]])