# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = 0
        result = head
        firstNode = head
        deletePre = None
        while(firstNode):
            count = count + 1
            if count == n + 1:
                deletePre = head
            firstNode = firstNode.next
            if not firstNode:
                break
            if deletePre:
                deletePre = deletePre.next
        if not deletePre:
            return result.next
        deleteValue = deletePre.next
        deletePre.next = deleteValue.next
        return result
        