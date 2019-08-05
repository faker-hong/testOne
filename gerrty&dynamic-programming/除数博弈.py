def divisorGame(N):
    """
    :type N: int
    :rtype: bool
    """
    if N <= 1:
        return False
    if N % 2 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(divisorGame(8))