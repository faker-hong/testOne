from collections import defaultdict
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]

        # 构建邻接表
        adjs = defaultdict(list)
        degrees = [0 for _ in range(n)]
        for (a, b) in edges:
            adjs[a].append(b)
            adjs[b].append(a)
            degrees[a] += 1
            degrees[b] += 1

        # 只有一条边
        layer = []
        for ind, val in enumerate(degrees):
            if val == 1:
                layer.append(ind)

        while layer:
            next_layer = []
            for node in layer:
                for neighbor in adjs[node]:
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        next_layer.append(neighbor)

            if not next_layer:
                return layer
            layer = next_layer