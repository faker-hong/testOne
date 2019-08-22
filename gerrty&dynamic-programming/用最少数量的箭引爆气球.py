class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) < 2:
            return len(points)
        points.sort(key=lambda x: x[0])
        res = 1
        end = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > end:
                end = points[i][1]
                res += 1
            else:
                end = min(end, points[i][1])
        return res


if __name__ == '__main__':
    s = Solution()
    points = [[10,16], [2,8], [1,6], [7,12]]
    s.findMinArrowShots(points)