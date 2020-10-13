# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not (preorder and inorder):
            return None

        # 根据前序遍历的第一个节点可以确定根节点
        root = TreeNode(preorder[0])
        # 用preorder[0]去中序数组中查找对应的元素
        mid_idx = inorder.index(preorder[0])
        # 递归的处理前序数组的左边部分和中序数组的左边部分
        # 递归的处理前序数组右边部分和中序数组的右边部分
        root.left = self.buildTree(preorder[1: mid_idx+1], inorder[:mid_idx])
        root.right = self.buildTree(preorder[mid_idx+1:], inorder[mid_idx+1:])

        return root


if __name__ == '__main__':
    s = Solution()
    s.buildTree([3,9,20,15,7], [9,3,15,20,7])
