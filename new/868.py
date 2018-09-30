class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        last_pos = -1
        now_pos = 0
        result = 0
        while(N > 0):
            v = (N & 1)
            if v == 1 and last_pos >= 0:
                result = max(result, now_pos - last_pos)
            last_pos = now_pos if v == 1 else last_pos
            now_pos += 1
            N = (N >> 1)
        return result