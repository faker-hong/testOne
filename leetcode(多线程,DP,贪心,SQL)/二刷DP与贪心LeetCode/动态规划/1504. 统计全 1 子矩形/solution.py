class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        if not mat or not mat[0]:
            return 0

        n = len(mat)
        m = len(mat[0])

        ans = 0
        dp = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if mat[i][j]:
                    dp[i][j] = dp[i][j-1] + 1
                    mmin = float('inf')
                    for k in range(i, -1, -1):
                        mmin = min(mmin, dp[k][j])
                        ans += mmin

        return ans