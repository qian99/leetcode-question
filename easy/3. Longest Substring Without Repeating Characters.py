class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0
        i = j = 0
        result = 0
        count = {}
        while (j < n):
            c = s[j]
            if not count.has_key(c):
                count[c] = 0
            count[c] += 1
            while(i < j and count[c] > 1):
                count[s[i]] -= 1
                i += 1
            result = max(result, j - i + 1)
            j = j + 1
        return result