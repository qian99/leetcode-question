class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        a = x
        b = 0
        while x > 0:
            b = b*10 + (x % 10)
            x = x // 10
        return a == b