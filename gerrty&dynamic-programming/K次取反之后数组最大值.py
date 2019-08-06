def largestSumAfterKNegations(A, K):
    """
    :type A: List[int]
    :type K: int
    :rtype: int
    """
    A.sort()
    for i in range(K):
        if A[i] < 0:
            A[i] = -A[i]
        else:
            A[i] -= 2 * ((K - i) % 2) * min(A[i], A[i - 1])
            # 根据奇偶性在数组判断是否减去最小整数，最后都是一起求和，所以只要把这一项加进数组就行
            break
    return sum(A)


if __name__ == '__main__':
    print(largestSumAfterKNegations([2,-3,-1,5,-4],4))