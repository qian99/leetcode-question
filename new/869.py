class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        max_value = 1e9
        power2values = {}
        mul_value = 1
        while mul_value < max_value:
            counts = [0 for i in xrange(10)]
            temp = mul_value
            while temp > 0:
                p = temp % 10
                counts[p] += 1
                temp = temp // 10
            power2values[''.join([str(v) for v in counts])] = True
            mul_value *= 2

        counts = [0 for i in xrange(10)]
        temp = N
        while temp > 0:
            p = temp % 10
            counts[p] += 1
            temp = temp // 10
        str_value = ''.join([str(v) for v in counts])
        return power2values.has_key(str_value)

s = Solution()
print s.reorderedPowerOf2(1)
print s.reorderedPowerOf2(10)
print s.reorderedPowerOf2(16)
print s.reorderedPowerOf2(24)
print s.reorderedPowerOf2(46)