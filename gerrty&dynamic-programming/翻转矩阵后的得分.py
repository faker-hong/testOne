def matrixScore(A):
    """
    :type A: List[List[int]]
    :rtype: int
    """
    for i in range(len(A)):  # 横向翻转
        if A[i][0] == 0:
            for j in range(len(A[0])):
                if A[i][j] == 0:
                    A[i][j] = 1
                else:
                    A[i][j] = 0

    for i in range(len(A[0])):  # 纵向翻转
        num1, num0 = 0, 0
        for j in range(len(A)):
            if A[j][i] == 1:
                num1 += 1
        num0 = len(A) - num1
        if num1 < num0:
            for j in range(len(A)):
                if A[j][i] == 0:
                    A[j][i] = 1
                else:
                    A[j][i] = 0

    res = 0
    for i in A:
        t = 0
        for j in i:
            t = t*2 + j

        res += t
    return res



if __name__ == '__main__':
    a =[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
    print(matrixScore(a))
