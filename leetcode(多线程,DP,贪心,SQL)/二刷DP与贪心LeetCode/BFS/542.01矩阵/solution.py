'''
输入:

0 0 0
0 1 0
1 1 1
输出:

0 0 0
0 1 0
1 2 1
给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。

两个相邻元素间的距离为 1 。
'''


# 把每个为0的位置放进队列，作为兄弟节点，
import collections


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0])
        dist = [[0] * n for _ in range(m)]

        # 找出0的位置
        zeros = [(i, j) for i in range(m) for j in range(n) if matrix[i][j] == 0]

        # 存放0位置的队列
        queue = collections.deque(zeros)
        visited = set(queue)

        while queue:
            i, j = queue.popleft()
            for ix, iy in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= ix < m and 0 <= iy < n and (ix, iy) not in visited:
                    dist[ix][iy] = dist[i][j] + 1
                    queue.append((ix, iy))
                    visited.add((ix, iy))

        return dist


if __name__ == '__main__':
    matrix = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    s = Solution()
    dist = s.updateMatrix(matrix)
    print(dist)