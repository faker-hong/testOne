class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        # 解题思路：假定每两个的左边都保持不变，右边如果是合法的那就不需要移动，如果不合法就找到合法的索引，并将两个数交换，
        # 所以就需要每两个的去循环遍历
        def find_match(n):
            if n % 2 == 0:
                return n + 1
            else:
                return n - 1

        c = 0
        for i in range(0, len(row), 2):
            a = row[i]
            b = find_match(a)
            if row[i+1] != b:
                ind = row.index(b)
                row[i+1], row[ind] = row[ind], row[i+1]
                c += 1
        return c


if __name__ == '__main__':
    s = Solution()
    s.minSwapsCouples([1,2,3,0])