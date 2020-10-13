from functools import lru_cache


class Solution(object):
    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        # 三个状态，t 走的步数， x 老鼠的位置， y 猫的位置
        @lru_cache(None)
        def search(t, x, y):
            # 老鼠到洞口最多走N步，如果总步数到达2N，那说明平局
            if t == int(len(graph) * 2):
                return 0

            # 如果x和y的位置相同，猫赢
            if x == y:
                return 2

            # 如果x的位置为0，老鼠赢
            if x == 0:
                return 1

            # 如果步数为偶数，是老鼠的回合，老鼠先走
            if t % 2 == 0:
                # 老鼠能在任何一个下一步获胜，也就是等于1，则返回1
                if any(search(t+1, x_cnt, y) == 1 for x_cnt in graph[x]):
                    return 1

                # 老鼠在任何一个下一步打成平局，返回0
                if any(search(t+1, x_cnt, y) == 0 for x_cnt in graph[x]):
                    return 0

                # 如果两者都不是，则猫获胜，返回2
                return 2
            else:
                # 这里是猫的回合
                # 如果猫能在任何下一回合获胜，返回2
                if any(search(t+1, x, y_cnt) == 2 for y_cnt in graph[y] if y_cnt != 0):
                    return 2

                # 如果猫在任何下一回事都是平局，返回0
                if any(search(t+1, x, y_cnt) == 0 for y_cnt in graph[y] if y_cnt != 0):
                    return 0

                # 都不是则老鼠赢，返回1
                return 1

        return search(0, 1, 2)  # 开始步数为0， 老鼠的位置为1， 猫的位置为2


if __name__ == '__main__':
    s = Solution()
    res = s.catMouseGame([[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]])
    print(res)