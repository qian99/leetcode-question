class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        addValue = 0
        result = node = ListNode(0)
        while(l1 != None or l2 != None or addValue > 0):
            x = y = 0
            if l1 != None:
                x = l1.val
            if l2 != None:
                y = l2.val
            sum = x + y + addValue
            addValue = 0
            if sum >= 10:
                addValue = 1
                sum = sum - 10
            node.next = ListNode(sum)
            node = node.next
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
        return result.next