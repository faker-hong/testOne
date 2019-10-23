def minimumTotal(triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    for i in range(1, len(triangle)):
        triangle[i][0] += triangle[i - 1][0]
        for j in range(1, len(triangle[i]) - 1):
            triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
        triangle[i][-1] += triangle[i - 1][-1]
    return min(triangle[-1])



if __name__ == '__main__':
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    res = minimumTotal(triangle)
    print(res)