from itertools import chain


class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        # 构图，直达车station_bus[i], 从i站点可乘坐的公交，从而可以知道可去的站点
        # h = set{} , 是否是换乘车站
        # level 换乘数
        # visit是去过的换乘站，去过的再去就是多余的
        # 结果只可能有两种，借助N个换乘车站到达，和直达
        # 每次，先判断是否直达，如果直达，结束，return level
        # 没有直达，找到所有的换乘车站level+=1
        # 没有找到返回-1

        # 判断routes中是否存在终点站T， 不存在直接返回-1
        if T not in list(chain.from_iterable(routes)):
            return -1

        if S == T:
            return 0

        # 做一个dict， 站点->经过此站点的公交集合的索引
        station_bus = {}
        for i in range(len(routes)):
            for j in routes[i]:
                if j in station_bus:
                    station_bus[j].add(i)
                else:
                    station_bus[j] = set({i})

        # 有至少两个公交经过的站台
        h = set()
        for key, value in station_bus.items():
            if len(value) > 1:
                h.add(key)

        visited = set({S})
        queue = [S]
        level = 1
        n = 1   # 这里出发站点S算一个换程车站

        while len(queue) > 0:
            front = queue.pop(0)
            for bus in station_bus[front]:
                if T in routes[bus]:    # 判断是否可以直达
                    return level

                for site in routes[bus]:    # 判断是否是换乘车站
                    if site in h and site not in visited:
                        queue.append(site)
                        visited.add(site)

            n -= 1
            if n == 0:
                n = len(queue)
                level += 1

        return -1


if __name__ == '__main__':
    routes = [[1, 2, 7], [3, 6, 7]]
    S = 1
    K = 6
    s = Solution()
    res = s.numBusesToDestination(routes, S, K)
    print(res)