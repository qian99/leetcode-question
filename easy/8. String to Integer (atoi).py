class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        n = len(str)
        if n == 0:
            return 0
        result = 0
        sign = 1
        leftL = 0
        while(leftL < n and str[leftL] == ' '):
            leftL += 1
        while(n - 1 > 0 and str[n - 1] == ' '):
            n -= 1
        if str[leftL] == '-':
            sign = -1
            leftL += 1
        elif str[leftL] == '+':
            sign = 1
            leftL += 1
        pos = leftL
        while (pos < n):
            if str[pos] < '0' or str[pos] > '9':
                break
            result = result*10 + int(str[pos])
            pos += 1
        result *= sign
        if result >= 0x80000000:
            result = 0x7FFFFFFF
        elif result < -(0x80000000):
            result = -0x80000000
        return result
        