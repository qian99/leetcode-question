# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        result = head
        preNode = None
        while(head):
            firstNode = head
            endNode = head
            count = 1
            while(endNode and endNode.next and count < k):
                endNode = endNode.next
                count += 1
            if count < k:
                break
            if not preNode:
                result = endNode
            else:
                preNode.next = endNode
            preNode = firstNode
            head = endNode.next
            while(count > 1):
                temp = firstNode.next
                firstNode.next = endNode.next
                endNode.next = firstNode
                firstNode = temp
                count = count - 1
        return result
                