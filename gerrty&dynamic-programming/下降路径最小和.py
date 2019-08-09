def minFallingPathSum(A):
    """
    :type A: List[List[int]]
    :rtype: int
    """
    dp = [[0]*len(A) for i in range(len(A[0]))]
    for i in range(len(A[0])):
        dp[0][i] = A[0][i]
    for i in range(1, len(A)):
        for j in range(len(A[0])):
            if j == 0:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j+1]) + A[i][j]
            elif j == len(A[0])-1:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + A[i][j]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j+1], dp[i-1][j-1]) + A[i][j]
    return min(dp[-1])


if __name__ == '__main__':
    A = [[1,2,3],[4,5,6],[7,8,9]]
    res = minFallingPathSum(A)
    print(res)