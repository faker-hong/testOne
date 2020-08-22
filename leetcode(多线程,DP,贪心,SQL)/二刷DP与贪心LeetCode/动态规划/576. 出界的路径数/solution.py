import collections


class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        memo = collections.defaultdict(int)

        def dfs(memo, i, j, k):
            if (i, j, k) not in memo:
                if i < 0 or i >= m or j < 0 or j >= n:
                    memo[(i, j, k)] = 1
                elif k > 0:
                    for x, y in [[i + 1, j], [i, j + 1], [i - 1, j], [i, j - 1]]:
                        memo[(i, j, k)] += dfs(memo, x, y, k - 1)
            return memo[(i, j, k)]

        dfs(memo, i, j, N)
        return memo[(i, j, N)] % MOD
