class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def dfs(left, right):
            # 递归终止条件
            # 两个都为空，两个有一个为空，值不想等
            if not (left or right):
                return True
            if not (left and right):
                return False
            if left.val != right.val:
                return False

            return dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root.left, root.right)