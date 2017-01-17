class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        isNeg = x < 0
        if isNeg:
            x = -x
        while x > 0:
            result = result * 10 + (x % 10)
            x = x // 10
        if isNeg:
            result = -result
        if abs(result) > 0x7FFFFFFF:
            return 0
        return result
        