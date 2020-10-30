# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def dfs(node, path):
            if not node.left and not node.right:
                path += str(node.val)
                res.append(int(path))

            if node.left:
                dfs(node.left, path + str(node.val))
            if node.right:
                dfs(node.right, path + str(node.val))

        res = []
        dfs(root, '')
        # print(res)
        return sum(res)