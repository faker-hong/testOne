def canCompleteCircuit(gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    for i in range(len(gas)):
        count = 0
        lists = []
        if gas[i] < cost[i]:
            continue
        else:
            for j in range(i, len(gas)+i):
                if j >= len(gas):
                    j = j - len(gas)
                count += gas[j] - cost[j]
                print(count, i)
                if count < 0:
                    break
                # print(j)
                # print(gas[j])
                lists.append(j)
            if len(lists) == len(gas):
                return lists[0]

    if len(lists) != len(gas):
        return -1
    else:
        return lists[0]


def canCompleteCircuitTwo(gas, cost):
    start = 0
    have = 0
    debt = 0
    for i in range(len(gas)):
        have += gas[i] - cost[i]
        if have < 0:
            start = i+1
            debt += have
            have = 0
    if have + debt >= 0 :
        return start
    else:
        return -1


if __name__ == '__main__':
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    gass = [3, 3, 4]
    costs = [3, 4, 4]
    # gas = [5, 1, 2, 3, 4]
    # cost = [4, 4, 1, 5, 1]
    print(canCompleteCircuitTwo(gas, cost))

