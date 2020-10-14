# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []

        def dfs(path, node):
            if node:
                if not node.left and not node.right:
                    path += str(node.val)
                    res.append(path)
                    return
                else:
                    path += str(node.val)
                    path += '->'

                    dfs(path, node.left)
                    dfs(path, node.right)

        dfs('', root)
        return res