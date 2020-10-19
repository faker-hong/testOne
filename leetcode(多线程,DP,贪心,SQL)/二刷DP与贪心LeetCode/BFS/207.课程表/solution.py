import collections


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # 记录每门课的入度，也就是先修课程的个数
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        queue = []

        # 这里adjacency的意义就是，当一门先修课程学完，需要先修这门课程的课的入度-1
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)

        for i in range(numCourses):
            if not indegrees[i]:
                queue.append(i)

        while queue:
            pre = queue.pop(0)
            numCourses -= 1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if indegrees[cur] == 0:
                    queue.append(cur)

        return numCourses <= 0


if __name__ == '__main__':
    s = Solution()
    res = s.canFinish(2, [[1, 0]])
    print(res)