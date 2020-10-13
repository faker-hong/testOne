# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(root):
            if not root:
                return 0
            height_left = dfs(root.left)
            height_right = dfs(root.right)

            if height_left == -1 or height_right == -1 or abs(height_right - height_left) > 1:
                return -1
            else:
                return max(height_right, height_left) + 1

        return dfs(root) >= 0