class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def helper(root, low=float("-inf"), high=float("inf")):
            if not root:
                return True

            val = root.val

            if val <= low or val >= high:
                return False

            if not helper(root.left, low, val):
                return False

            if not helper(root.right, val, high):
                return False

            return True

        return helper(root)