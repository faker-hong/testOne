def candy(ratings):

    num = [1]*len(ratings)

    for i in range(len(ratings)-1):
        if ratings[i] < ratings[i+1]:
            num[i+1] = num[i] + 1

    for i in range(len(ratings)-1, 0, -1):
        if ratings[i] < ratings[i-1]:
            num[i-1] = max(num[i-1], num[i]+1)

    return sum(num)


if __name__ == '__main__':
    a = [1, 0, 2]
    print(candy(a))