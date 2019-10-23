def carPooling(trips, capacity):
    """
    :type trips: List[List[int]]
    :type capacity: int
    :rtype: bool
    """
    # 题目规定距离为0-1000，距离都是相对起点0的距离
    # 在相应的位置加减人数，只要一路上一直没有超过capacity就说明可以全部接送
    locations = [0 for _ in range(1001)]
    for num, start, end in trips:
        locations[start] += num
        locations[end] -= num

    for i, num in enumerate(locations):
        locations[i] += locations[i-1]
        if locations[i] > capacity:
            return False
    return True


if __name__ == '__main__':
    trips = [[7,5,6],[6,7,8],[10,1,6]]
    capacity = 16
    print(carPooling(trips, capacity))