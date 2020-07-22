class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root, target, K):
        if not root:
            return []

        pmap = self.get_graph(root, None, {})

        '''区别：是从target开始BFS，而不是root'''
        queue = [target]
        '''用于判断是否check过这个节点，用in能够达到O(1)的查询'''
        check = {}
        cur_level = 0

        '''BFS每一层就代表distance的距离，第一层就是distance=1'''
        while cur_level != K:
            nxt = []
            for node in queue:
                if node not in check:
                    check[node] = 1
                    if node.left and node.left not in check:
                        nxt.append(node.left)
                    if node.right and node.right not in check:
                        nxt.append(node.right)
                    if node in pmap and pmap[node] not in check:
                        nxt.append(pmap[node])
            cur_level += 1
            queue = nxt

        return [node.val for node in queue]

    '''将tree转为undirected graph，记录父节点'''

    def get_graph(self, root, parent, pmap):
        if not root:
            return pmap
        if parent:
            pmap[root] = parent
        self.get_graph(root.left, root, pmap)
        self.get_graph(root.right, root, pmap)
        return pmap
