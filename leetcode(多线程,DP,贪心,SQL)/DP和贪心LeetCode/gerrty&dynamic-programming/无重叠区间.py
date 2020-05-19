class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        n = len(intervals)
        if n <= 1:
            return 0
        intervals = sorted(intervals, key=lambda i: i[1])
        i = 1
        count = 1
        cur_end = intervals[0][1]
        while i < n:
            if intervals[i][0] >= cur_end:
                count += 1
                cur_end = intervals[i][1]
                i += 1
            else:
                i += 1
        print(n-count)
        return n - count


if __name__ == '__main__':
    s = Solution()
    s.eraseOverlapIntervals([ [1,2], [2,7], [3,4], [4,6] ])