class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        def isLetter(c):
            return (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z')
        n = len(s) - 1
        count = 0
        while (n >= 0):
            is_letter = isLetter(s[n])
            if count == 0 and (not is_letter):
                n -= 1
                continue
            if is_letter:
                count += 1
            elif s[n] == ' ':
                break
            else:
                count = 0
                break
            n -= 1
        return count


res = Solution()
print res.lengthOfLastWord("hello world!")