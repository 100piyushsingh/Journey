# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s = 0
        c = 0
        prev = ListNode(0)
        prev1 = prev
        while l1 and l2:
            s = l1.val + l2.val + c
            c = s/10
            Node = ListNode(s%10)
            prev1.next = Node
            prev1 = Node
            l1 = l1.next
            l2 = l2.next
        while l1:
            s = l1.val + c
            c = s/10
            Node = ListNode(s%10)
            prev1.next = Node
            prev1 = Node
            l1 = l1.next
            
        while l2:
            s = l2.val + c
            c = s/10
            Node = ListNode(s%10)
            prev1.next = Node
            prev1 = Node
            l2 = l2.next
        if c == 1:
            prev1.next = ListNode(1)
        return prev.next
