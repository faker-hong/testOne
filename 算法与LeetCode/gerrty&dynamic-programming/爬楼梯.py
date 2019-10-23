def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    a = 0
    b = 1
    sum = 0
    for i in range(n):
        sum = a + b
        a = b
        b = sum
    return sum

if __name__ == '__main__':
    print(climbStairs(10))