class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        n = len(matrix)
        m = len(matrix[0])

        row, col = n-1, 0

        while row >= 0 and col < m:
            if matrix[row][col] < target:
                col += 1
            elif matrix[row][col] > target:
                row -= 1
            else:
                return True

        return False


if __name__ == '__main__':
    matrix = [[]]
    target = 1
    s = Solution()
    s.findNumberIn2DArray(matrix, target)