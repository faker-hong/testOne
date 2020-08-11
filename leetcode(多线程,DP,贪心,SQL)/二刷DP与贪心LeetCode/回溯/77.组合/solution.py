class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []

        def helper(j, temp):
            if len(temp) == k:
                res.append(temp)
                return

            for i in range(j, n + 1):
                helper(i + 1, temp + [i])

        helper(1, [])
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.combine(4, 2)
    print(res)