class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return

        # 用两个set记录能流入太平洋和大西洋的坐标，然后取两个集合的交集
        row, col = len(matrix), len(matrix[0])
        res1 = set()    # 太平洋，也就是能流入左上的坐标
        res2 = set()    # 大西洋，也就是能流入右下的坐标

        def dfs(i, j, res):
            res.add((i, j))

            for x, y in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                if 0 <= x < row and 0 <= y < col and matrix[x][y] >= matrix[i][j] and (x, y) not in set:
                    dfs(x, y, res)

        # 流入太平洋
        for i in range(row):
            dfs(i, 0, res1)

        for j in range(col):
            dfs(0, j, res1)

        # 流入大西洋
        for i in range(row):
            dfs(i, col-1, res2)

        for j in range(col):
            dfs(row-1, j, res2)

        return res1&res2