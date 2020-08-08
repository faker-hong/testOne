class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []

        queue = [root]
        res = []

        while queue:
            n = len(queue)
            next_layer = []
            cur_val = []
            for i in range(n):
                p = queue.pop(0)
                cur_val.append(p.val)
                if p.children:
                    for child in p.children:
                        next_layer.append(child)

            res.append(cur_val)
            queue = next_layer

        return res