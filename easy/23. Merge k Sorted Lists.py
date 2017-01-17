# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        q = PriorityQueue()
        for node in lists:
            if node:
                q.put((node.val,node))
        result = ListNode(0)
        temp = result
        while(q.qsize() > 0):
            node = q.get()[1]
            temp.next = ListNode(node.val)
            temp = temp.next
            node = node.next
            if node :
                q.put((node.val,node))
        return result.next