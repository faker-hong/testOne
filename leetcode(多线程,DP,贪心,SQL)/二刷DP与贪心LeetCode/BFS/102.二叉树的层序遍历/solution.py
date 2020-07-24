# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        queue = [root]
        res = []
        n = 1
        cur_layer_val = []
        next_layer = []

        while queue:
            node = queue.pop(0)
            n -= 1
            cur_layer_val.append(node.val)
            if node.left:
                next_layer.append(node.left)
            if node.right:
                next_layer.append(node.right)

            if n == 0:  # 判断当前层，是否还有节点，没有节点则遍历下一层
                n = len(next_layer)
                res.append(cur_layer_val)
                queue = next_layer
                next_layer = []
                cur_layer_val = []

        return res


if __name__ == '__main__':
    T = TreeNode(3)
    T.left = TreeNode(9)
    T.right = TreeNode(20)
    T.right.left = TreeNode(15)
    T.left.right = TreeNode(7)

    s = Solution()
    res = s.levelOrder(T)

    print(res)