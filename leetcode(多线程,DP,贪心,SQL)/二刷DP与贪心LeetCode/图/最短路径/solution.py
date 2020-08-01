def seachPath(graph, start, end):
    result = []
    generatePath(graph, [start], end, result)
    result.sort(key=lambda x: len(x))
    return result


def generatePath(graph, path, end, result):
    node = path[-1]
    if node == end:
        result.append(path)
    else:
        for e in graph[node]:
            if e not in path:
                generatePath(graph, path + [e], end, result)


if __name__ == '__main__':
    # 构建树
    Graph = {
        'A':  ['B', 'C', 'D'],
        'B':  ['E'],
        'C':  ['D', 'F'],
        'D':  ['B', 'E', 'G'],
        'E':  [],
        'F':  ['D', 'G'],
        'G':  ['E']}

    result = seachPath(Graph, 'A', 'G')
    for i in result:
        print(i)