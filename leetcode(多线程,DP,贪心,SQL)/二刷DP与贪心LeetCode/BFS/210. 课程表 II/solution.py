class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        indegrees = [0 for _ in range(numCourses)]
        adjagency = [[] for _ in range(numCourses)]
        queue = []
        res = []

        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjagency[pre].append(cur)

        for i, num in enumerate(indegrees):
            if num == 0:
                queue.append(i)

        while queue:
            n = queue.pop(0)
            res.append(n)
            for node in adjagency[n]:
                indegrees[node] -= 1
                if indegrees[node] == 0:
                    queue.append(node)

        return res if len(res) == numCourses else []


if __name__ == '__main__':
    s = Solution()
    res = s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
    print(res)