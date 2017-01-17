class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        hashChar = { ')' : '(', ']':'[' , '}' : '{'}
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif len(stack):
                topValue = stack.pop()
                if topValue != hashChar[c]:
                    return False
            else:
                return False
        return len(stack) == 0