def minDeletionSize(A):
    res = 0
    for i in zip(*A):
        if list(i) == sorted(i):
            res += 1
    return res

if __name__ == '__main__':
    A = ["rrjk","furt","guzm"]
    res = minDeletionSize(A)
    print(res)