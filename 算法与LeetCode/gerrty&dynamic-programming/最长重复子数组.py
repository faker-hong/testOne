def findLength(A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: int
    倒着遍历比较A[i:]与B[j:]相同部分，如果A[i] == B[j],就拿dp[i+1][j+1]的值再+1
    """
    dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
    for i in range(len(A) - 1, -1, -1):
        for j in range(len(B) - 1, -1, -1):
            if A[i] == B[j]:
                dp[i][j] = dp[i + 1][j + 1] + 1
    return max(max(row) for row in dp)


if __name__ == '__main__':
    A = [1, 2, 3, 2, 1]
    B = [3, 2, 1, 4, 7]
    print(findLength(A,B))
