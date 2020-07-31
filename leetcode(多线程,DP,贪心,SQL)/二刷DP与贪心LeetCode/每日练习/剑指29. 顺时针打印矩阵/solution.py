class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        res = []

        # 行和列
        row = len(matrix)
        col = len(matrix[0])

        # 设置四个遍历方向
        left = 0
        right = col - 1
        upper = 0
        down = row - 1

        while len(res) < col * row:
            # 先从左向右遍历
            for i in range(left, right + 1):
                res.append(matrix[upper][i])
                if len(res) == col * row:
                    return res
            upper += 1

            # 从上到下遍历
            for i in range(upper, down + 1):
                res.append(matrix[i][right])
                if len(res) == col * row:
                    return res
            right -= 1

            # 从右往左遍历
            for i in range(right, left - 1, -1):
                res.append(matrix[down][i])
                if len(res) == col * row:
                    return res
            down -= 1

            # 从下往上遍历
            for i in range(down, upper - 1, -1):
                res.append(matrix[i][left])
                if len(res) == col * row:
                    return res
            left += 1

        return res
