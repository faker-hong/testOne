class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        def dfs(head):
            if not head:
                return Node
            if head in visit:
                return visit[head]

            copy = Node(head.val, None, None)
            visit[head] = copy
            copy.next = dfs(head.next)
            copy.random = dfs(head.random)
            return copy

        visit = {}
        return dfs(head)