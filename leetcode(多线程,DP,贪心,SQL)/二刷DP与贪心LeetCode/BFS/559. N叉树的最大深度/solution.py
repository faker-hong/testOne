"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        queue = [root]
        depth = 0

        while queue:
            next_layer = []
            n = len(queue)

            for i in range(n):
                node = queue.pop(0)
                if node.children:
                    for j in range(len(node.children)):
                        next_layer.append(node.children[j])

            queue = next_layer
            depth += 1

        return depth