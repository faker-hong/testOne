# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        queue = [root]
        res = []

        while queue:
            next_layer = []
            last_node = queue[-1]
            res.append(last_node.val)
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append((node.right))
            queue = next_layer
        # print(res)
        return res


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node1.right = node2
    s = Solution()
    s.rightSideView(node1)