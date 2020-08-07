class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 判断皇后位置是否合法
        def is_valid(row, col, track):
            if col in track:
                return False

            for k in range(row):
                if row + col == k + track[k] or row - col == k - track[k]:
                    return False

            return True

        def backtrack(row, track):
            if row == n:
                res.append(track)

            for col in range(n):
                if is_valid(row, col, track):
                    backtrack(row + 1, track + [col])

        res = []
        backtrack(0, [])

        return len(res)