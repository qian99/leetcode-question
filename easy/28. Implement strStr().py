class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)
        if m == 0:
            return 0
        next = [0 for i in range(m)]
        i = 1
        while(i < m - 1):
            j = next[i]
            while(j > 0 and needle[j] != needle[i]):
                j = next[j]
            if needle[j] == needle[i]:
                next[i + 1] = j + 1
            else:
                next[i + 1] = 0
            i += 1
    
        i = j = 0
        while i < n:
            while(j > 0 and haystack[i] != needle[j]):
                j = next[j]
            if haystack[i] == needle[j]:
                j += 1
                if j == m:
                    return i - m + 1
            i += 1
        return -1