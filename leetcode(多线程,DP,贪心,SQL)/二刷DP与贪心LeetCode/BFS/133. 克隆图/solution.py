"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return []

        clone = Node(node.val, [])
        queue = [node]
        visit = {}
        visit[node] = clone

        while queue:
            tmp = queue.pop()

            for n in tmp.neighbors:
                if n not in visit:
                    visit[n] = Node(n.val, [])
                    queue.append(n)
                visit[tmp].neighbors.append(visit[n])
        return clone