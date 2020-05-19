class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        area = 0

        dp = [[0]*len(matrix[0]) for i in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    continue
                # 这一步用于计算每行中的宽，width
                width = dp[i][j] = dp[i][j - 1] + 1 if j else 1
                # 遍历当前列，取width小的为宽，高度为i-k+1。
                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    area = max(area, width*(i-k+1))
        return area

    def maximalRectangle_two(self, matrix):
        if not matrix: return 0

        m = len(matrix)
        n = len(matrix[0])

        left = [0] * n
        right = [n] * n
        height = [0] * n

        maxarea = 0

        for i in range(m):

            cur_left, cur_right = 0, n
            # 高度
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            # 左边界
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1
            # 右边界
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
            # 面积
            for j in range(n):
                maxarea = max(maxarea, height[j] * (right[j] - left[j]))

        return maxarea


if __name__ == '__main__':
    s = Solution()
    matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

    re = s.maximalRectangle_two(matrix)
    print(re)