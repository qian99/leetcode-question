class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)
        max_value = n + m
        dp = [[max_value for j in range(m + 1)] for i in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][0] = i
        for j in range(1, m + 1):
            dp[0][j] = j
        dp[0][0] = 0
        for i in xrange(1, n + 1):
            c1 = word1[i - 1]
            for j in xrange(1, m + 1):
                c2 = word2[j - 1]
                if c1 == c2:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 1)
        return dp[n][m]

s = Solution()
print s.minDistance('intention', 'execution')
print s.minDistance('', 'a')
print s.minDistance('sss', 'ss')
print s.minDistance('sea', 'eat')