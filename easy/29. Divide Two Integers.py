class Solution(object):
    def divide(self, dividend, divisor):
        res = 0
        neg = 1
        if dividend < 0:
            dividend *= -1
            neg *= -1
        if divisor < 0:
            divisor *= -1
            neg *= -1
        while dividend >= divisor:
            value = divisor
            count = 1
            while dividend >= value:
                dividend -= value
                res += count
                count <<= 1
                value <<= 1
        res *= neg
        return min(max(-2147483648, res), 2147483647)