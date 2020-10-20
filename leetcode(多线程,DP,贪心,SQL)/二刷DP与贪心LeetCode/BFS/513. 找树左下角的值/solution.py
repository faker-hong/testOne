# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return root

        queue = [root]

        while queue:
            next_layer = []
            n = len(queue)
            res = None

            for i in range(n):
                node = queue.pop()
                res = node.val
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)

            queue = next_layer
            if not queue:
                return res

    def opt_findBottomLeftValue(self, root):
        if not root:
            return

        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return node.val