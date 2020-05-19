'''
给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例:

输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6
'''


# 执行速度和内存消耗较高，但能通过
def maximalRectangle(matrix):
    maxArea = 0

    dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '0':
                continue

            # 计算宽度
            width = dp[i][j] = dp[i][j - 1] + 1 if j else 1

            # 计算最大面积
            for k in range(i, -1, -1):
                width = min(width, dp[k][j])
                maxArea = max(maxArea, width*(i-k+1))
    return maxArea


def maximalRectangle(matrix):
    if not matrix:
        return 0

    # 行和列
    m = len(matrix)
    n = len(matrix[0])

    # 初始化长宽高
    left = [0] * n
    right = [n] * n
    height = [0] * n

    maxArea = 0

    for i in range(m):
        cur_left, cur_right = 0, n

        # 更新height
        for j in range(n):
            if matrix[i][j] == '1':
                height[j] += 1
            else:
                height[j] = 0

        # 更新left
        for j in range(n):
            if matrix[i][j] == '1':
                left[j] = max(left[j], cur_left)
            else:
                left[j] = 0
                cur_left = j + 1

        # 更新right
        for j in range(n-1, -1, -1):
            if matrix[i][j] == '1':
                right[j] = min(right[j], cur_right)
            else:
                right[j] = n
                cur_right = j

        # 更新maxArea
        for j in range(n):
            maxArea = max(maxArea, height[j] * (right[j] - left[j]))

    return maxArea


if __name__ == '__main__':
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    area = maximalRectangle(matrix)
    print(area)