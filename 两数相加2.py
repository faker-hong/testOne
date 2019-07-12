# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)
        re = l3
        flag = 0
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        while ( l1 or l2):
            sum = 0 
            if l1:
                sum = l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            sumpre = ((sum + flag) % 10)
            flag = ((sum + flag) // 10)
            re.next = ListNode(sumpre)
            re = re.next
        if flag:
            re.next = ListNode(1)
        re = l3.next
        del l3
        return re