# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result = head
        pre = None
        while(head and head.next):
            next = head.next
            if pre:
                pre.next = next
            else:
                result = next
            head.next = next.next
            next.next = head
            pre = head
            head = head.next
        return result
        