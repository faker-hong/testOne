# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def __init__(self):
        self.memo = {}

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0

        if self.memo.has_key(root):
            return self.memo[root]

        # 这里两个选择，偷当前节点，和不偷当前节点
        # 直接相连的节点不能都偷，所以这里偷了当前节点，就要偷下下个节点
        do_it = root.val + (0 if root.left == None else (self.rob(root.left.left) + self.rob(root.left.right))) + (
            0 if root.right == None else (self.rob(root.right.left) + self.rob(root.right.right)))

        # 这里选择偷下一个节点
        not_do = self.rob(root.left) + self.rob(root.right)

        max_money = max(do_it, not_do)
        self.memo[root] = max_money
        return max_money
