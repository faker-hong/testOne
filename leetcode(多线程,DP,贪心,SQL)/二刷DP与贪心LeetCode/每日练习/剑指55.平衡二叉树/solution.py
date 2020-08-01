class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(root):
            if not root:
                return (True, 0)

            l, r = helper(root.left), helper(root.right)

            return abs(l[1] - r[1]) < 2 and l[0] and r[0], max(l[1], r[1]) + 1

        return helper(root)[0]