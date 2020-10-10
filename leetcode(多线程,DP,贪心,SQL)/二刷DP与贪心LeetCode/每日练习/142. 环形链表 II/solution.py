# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        visit = {None}

        while head not in visit:
            visit.add(head)
            head = head.next

        return head

    # 快慢指针
    '''
    还有一个纯数学的快慢指针解法，设环的起始节点为 E，快慢指针从 head 出发，快指针速度为 2，设相交节点为 X，
    head 到 E 的距离为 H，E 到 X 的距离为 D，环的长度为 L，那么有：快指针走过的距离等于慢指针走过的距离加
    快指针多走的距离（多走了 n 圈的 L） 2(H + D) = H + D + nL，因此可以推出 H = nL - D，这意味着如果我们
    让俩个慢指针一个从 head 出发，一个从 X 出发的话，他们一定会在节点 E 相遇
    '''
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        else:
            return None

        while head is not slow:
            head = head.next
            slow = slow.next

        return head
