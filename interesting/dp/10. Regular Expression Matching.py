class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        partten = []
        realPartten = ""
        lenp = len(p)
        for i in range(lenp):
            if i > 0 and p[i] == '*' and p[i - 1] == '*':
                continue
            realPartten += p[i]
        n = len(s)
        m = len(realPartten)
        dp = [[False]*(n + 1) for i in range(m + 1)]
        dp[0][0] = True
        i = 1
        while (i <= m):
            if realPartten[i - 1] == '*' or i + 1 <= m and realPartten[i] == '*':
                dp[i][0] = dp[i - 1][0]
            j = 1
            while(j <= n):
                if realPartten[i - 1] == '*':
                    dp[i][j] = dp[i - 1][j]
                elif i + 1 <= m and realPartten[i] == '*':
                    if s[j - 1] == realPartten[i - 1] or realPartten[i - 1] == '.':
                        dp[i][j] = dp[i - 1][j - 1] or dp[i][j - 1] or dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i - 1][j]
                elif s[j - 1] == realPartten[i - 1] or realPartten[i - 1] == '.':
                    dp[i][j] = dp[i][j] or dp[i - 1][j - 1]
                j += 1
            i += 1
        return dp[m][n]