class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row = len(board)
        col = len(board[0])

        def backtrack(i, j, k, visited):
            if k == len(word):
                return True

            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x = i + x
                new_y = j + y

                if 0 <= new_x < row and 0 <= new_y < col and (new_x, new_y) not in visited and board[new_x][new_y] == word[k]:
                    visited.add((new_x, new_y))
                    if backtrack(new_x, new_y, k + 1, visited):
                        return True
                    visited.remove((new_x, new_y))

            return False

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0] and backtrack(i, j, 1, {(i, j)}):
                    return True

        return False


if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    s = Solution()
    res = s.exist(board, word)
    print(res)