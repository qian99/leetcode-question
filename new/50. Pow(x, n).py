class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        result = 1
        neg = 0
        if n < 0:
            neg = 1
            n = -n
        while(n > 0):
            if (n & 1):
                result *= x
            x *= x
            n >>= 1
        if neg > 0:
            result = 1.0/result
        return result

res = Solution()
print res.myPow(2,-3)