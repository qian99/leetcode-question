class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        invert = max(numRows - 2,0)
        result = ""
        n = len(s)
        for i in range(numRows):
            j = i
            while(j < n):
                result += s[j]
                k = (numRows - i - 1) + (invert - i + 1)
                add = numRows + invert
                if k != add and k != 0 and j + k < n:
                    result += s[j + k]
                j += add
        return result