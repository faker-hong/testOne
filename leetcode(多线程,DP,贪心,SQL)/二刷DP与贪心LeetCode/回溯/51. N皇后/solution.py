class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # 判断放置的皇后位置与之前的是否冲突
        def is_valid(row, col, track):
            # 因为每一次的row不同，所以不用判断是否在同一行
            if col in track:    # 是否在同一列
                return False
            # 判断是否在两条对角线上
            for k in range(row):
                if row + col == k + track[k] or row - col == k - track[k]:
                    return False

            return True

        def backtrack(row, track):
            if row == n:
                res.append(track)
                return

            for col in range(n):
                if is_valid(row, col, track):   # 位置合法，进入下一行
                    backtrack(row + 1, track + [col])

        res = []
        backtrack(0, [])

        return [['.'*i + 'Q' + '.'*(n-i-1) for i in l] for l in res]


if __name__ == '__main__':
    s = Solution()
    res = s.solveNQueens(4)
    print(res)