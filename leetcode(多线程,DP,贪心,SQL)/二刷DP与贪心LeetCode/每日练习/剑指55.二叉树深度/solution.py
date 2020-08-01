class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def helper(root):
            if not root:
                return 0

            l, r = helper(root.left), helper(root.right)
            return max(l, r) + 1

        return helper(root)