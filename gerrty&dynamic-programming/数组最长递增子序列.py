def longgstSubsequence(arr):
    num = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[i] > arr[j] and num[j]+1 > num[i]:
                num[i] = num[j] + 1

    max = sorted(num)[-1]
    return max


if __name__ == '__main__':
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print(longgstSubsequence(arr))
