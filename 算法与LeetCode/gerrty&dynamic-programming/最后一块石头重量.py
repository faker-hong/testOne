def lastStoneWeight(stones):
    """
    :type stones: List[int]
    :rtype: int
    """
    new_stones = sorted(stones)
    while len(new_stones) >= 2:
        new_stones = sorted(new_stones)
        a = new_stones.pop()
        b = new_stones.pop()
        new_stone = a-b
        if new_stone != 0:
            new_stones.append(new_stone)

    if len(new_stones) == 0:
        return 0
    else:
        return new_stones[0]


if __name__ == '__main__':
    a= [1,2,3,4]
    print(lastStoneWeight(a))

