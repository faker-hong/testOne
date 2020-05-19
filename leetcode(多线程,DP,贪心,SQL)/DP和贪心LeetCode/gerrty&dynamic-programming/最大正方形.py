class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        height = len(matrix)
        width = len(matrix[0])
        dp = [[0]*(1+width) for i in range(height+1)]
        max_length = 0
        for i in range(1, height+1):
            for j in range(1, width+1):
                if matrix[i-1][j-1] == 1:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                    max_length = max(dp[i][j], max_length)
        print(dp)
        return max_length**2


if __name__ == '__main__':
    s = Solution()
    mar = [[1,1,1],[1,1,1]]
    print(s.maximalSquare(mar))