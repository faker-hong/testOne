# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """
        def cur(A, B):
            if not B:
                return True
            if not A or A.val != B.val:
                return False
            return cur(A.left, B.left) and cur(A.right, B.right)

        return bool(A and B) and (cur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))

