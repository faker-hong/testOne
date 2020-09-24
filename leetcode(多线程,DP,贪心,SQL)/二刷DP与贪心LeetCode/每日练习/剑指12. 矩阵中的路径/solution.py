'''
[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

矩阵中存在一条路径包含这个字符串，走过的格子不能再走


思路：
    1.根据word的第一个字符，找到对应坐标
    2.根据深度优先算法进行搜索
'''


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(x, y, visit):
            if len(visit) == len(word):
                return True

            for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_x = x + i
                new_y = y + j
                # 判断节点是否有效
                if 0 <= new_x < n and 0 <= new_y < m and board[new_x][new_y] == word[len(visit)] and (new_x, new_y) not in visit:
                    visit.add((new_x, new_y))
                    # 回溯
                    if dfs(new_x, new_y, visit):
                        return True
                    # 失败后将此路径开通，也就是在集合中删掉
                    visit.discard((new_x, new_y))

            return False

        n = len(board)
        m = len(board[0])
        # 找出首字符的坐标
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and dfs(i, j, {(i, j)}):
                    return True
        return False


if __name__ == '__main__':
    # board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    # word = "ABCCED"
    # board = [["a", "a"], ["c", "d"]]
    # word = "abcd"
    board = [["a", "a"]]
    word = 'aaa'
    # board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    # word = "SEE"
    s = Solution()
    res = s.exist(board, word)
    print(res)