class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # 先做排序，按结束位置升序，如果起始位置相同则降序
        intervals.sort(key=lambda x: (x[1], -x[0]))
        re = [-1, -1]

        # 这里有三种情况，一是无交集，有一个交集，2个及以上交集
        for x in intervals:
            # 两个及以上交集就不用处理
            if x[0] <= re[-2]:
                continue
            # 无交集就要放最大的两个树，x[1]-1与x[1]
            if x[0] > re[-1]:
                re.append(x[1]-1)
            # 一个交集就把最大的数塞进集合
            re.append(x[1])
        return len(re) - 2


if __name__ == '__main__':
    s = Solution()
    intervals = [[1, 3], [1, 4], [2, 5], [3, 5]]
    re = s.intersectionSizeTwo(intervals)