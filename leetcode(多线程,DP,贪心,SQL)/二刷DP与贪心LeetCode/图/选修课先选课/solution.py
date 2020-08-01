# 要选修c，需要修的课程的顺序
graph = {
    "a": ["b","d"],
    "b": ["c"],
    "d": ["e","c"],
    "e": ["c"],
    "c": [],
}

graph = {
    "5": ["2", "0"],
    "4": ["0", "1"],
    "2": ["3"],
    "3": ["1"],
    "0": [],
    "1": []
}


def TopologicalSort(graph):
    degrees = dict((v, 0) for v in graph)
    # print(degrees)

    for v in graph:
        for g in graph[v]:
            degrees[g] += 1

    # print(degrees)
    res = []
    queue = [v for v in degrees if degrees[v] == 0]
    # print(queue)

    while queue:
        q = queue.pop(0)
        res.append(q)
        for e in graph[q]:
            degrees[e] -= 1
            if degrees[e] == 0:
                queue.append(e)

    print(res)

TopologicalSort(graph)