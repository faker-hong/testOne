def twoCitySchedCost(costs):
    """
    :type costs: List[List[int]]
    :rtype: int
    """
    a = []
    sum = 0
    # costs.sort(key=lambda x: x[0]-x[1])
    for i in range(len(costs)-1):
        for j in range(len(costs)-i-1):
            if costs[j][0] - costs[j][1] > costs[j + 1][0] - costs[j + 1][1]:
                a = costs[j]
                costs[j] = costs[j + 1]
                costs[j+1] = a

    for i in range(len(costs)//2):
        sum += costs[i][0] + costs[i+len(costs)//2][1]

    return costs




if __name__ == '__main__':
    costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]

    print(twoCitySchedCost(costs))