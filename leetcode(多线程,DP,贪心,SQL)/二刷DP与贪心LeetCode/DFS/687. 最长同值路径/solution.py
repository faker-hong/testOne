# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            left_val = right_val = 0
            if root.left and root.left.val == root.val:
                left_val = left + 1

            if root.right and root.right.val == root.val:
                right_val = right + 1

            self.res = max(self.res, left_val + right_val)
            return max(left_val, right_val)

        dfs(root)
        return self.res