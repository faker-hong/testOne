class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """

        def find_match(x):
            if x % 2 == 0:
                return x + 1
            if x % 2 == 1:
                return x - 1

        times = 0
        for i in range(0, len(row), 2):
            a = row[i]
            b = find_match(a)
            if row[i + 1] != b:
                idx = row.index(b)
                row[i + 1], row[idx] = row[idx], row[i + 1]
                times += 1

        return times


if __name__ == '__main__':
    row = [0, 2, 1, 3]
    s = Solution()
    res = s.minSwapsCouples(row)
    print(res)