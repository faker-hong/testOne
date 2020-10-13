class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        path = []

        def dfs(p):
            path.append(p)
            if p == len(graph) - 1:
                res.append(path[:])
                path.pop()
                return
            for x in graph[p]:
                dfs(x)
            path.pop()

        dfs(0)
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]])
    print(res)