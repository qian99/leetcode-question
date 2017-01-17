#Manacher algorithm
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ss = "#"
        for i in range(len(s)):
            ss += s[i]
            ss += "#"
        pos = maxRight = 0
        maxp = 0
        n = len(ss)
        p = [0 for i in range(n)]
        for i in range(n):
            j = 2 * pos - i
            if j > 0 and i <= maxRight:
                p[i] = min(p[j], maxRight - i)
            else:
                p[i] = 0
            while (i + p[i] + 1 < n and i - p[i] - 1 >= 0 and ss[i + p[i] + 1] == ss[i - p[i] - 1]):
                p[i] += 1
            if i + p[i] > maxRight:
                maxRight = i + p[i]
                pos = i
                if p[i] > p[maxp]:
                    maxp = i
        start = maxp - p[maxp]
        end = maxp + p[maxp]
        result = ""
        while (start <= end):
            if ss[start] != "#":
                result += ss[start]
            start += 1
        return result
        