# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        queue = []
        p = head

        while p.next:
            queue.append(p.next)
            p = p.next

        i = 0
        j = len(queue) - 1

        while i < j:
            queue[i].next = queue[j]
            i += 1
            if i == j:
                break
            queue[j].next = queue[i]
            j -= 1

        queue[i].next = None


if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4

    s = Solution()
    s.reorderList(n1)