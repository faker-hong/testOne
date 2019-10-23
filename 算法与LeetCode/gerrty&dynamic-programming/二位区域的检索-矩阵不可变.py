class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.d = matrix
        m = len(self.d)
        if m > 0:
            n = len(self.d[0])
            self.d += [[0] * (n + 1)]
        for i in range(m):
            self.d[i] += [0]
            for j in range(n):
                self.d[i][j] += self.d[i - 1][j] + self.d[i][j - 1] - self.d[i - 1][j - 1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        # 超出时间限制
        # res = 0
        # for i in range(row1, row2+1):
        #     res += sum(self.martrix[i][col1:col2+1])
        # return res

        # 大面积减去小面积，加上重复减的区域
        return self.d[row2][col2] - self.d[row2][col1 - 1] - self.d[row1 - 1][col2] + self.d[row1 - 1][col1 - 1]


if __name__ == '__main__':
    matrix = NumMatrix([
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
])
    res = matrix.sumRegion(1,2,2,4)
    print(res)