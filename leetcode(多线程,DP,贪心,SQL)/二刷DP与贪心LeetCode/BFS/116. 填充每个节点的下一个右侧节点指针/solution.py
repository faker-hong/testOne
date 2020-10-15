"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root

        queue = [root]

        while queue:
            n = len(queue)

            while n:
                node = queue.pop(0)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                n -= 1

                if n != 0:
                    node.next = queue[0]
                else:
                    node.next = None

        return root