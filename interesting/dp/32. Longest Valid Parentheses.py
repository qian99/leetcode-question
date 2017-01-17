class Solution(object):
    def longestValidParentheses(self, s):
        n = len(s)
        result = 0
        dp = [0 for i in range(n + 1)]
        i = 1
        while i <= n:
            j = i - 1
            if s[j] == '(':
                dp[i] = 0
            elif j > 0:
                if s[j - 1] == '(':
                    dp[i] = dp[i - 2] + 2
                elif s[j - 1] == ')' and j - dp[i - 1] - 1 >= 0 and s[j - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + 2
                    if i - dp[i - 1] - 2 >= 0:
                        dp[i] += dp[i - dp[i - 1] - 2]
            result = max(dp[i], result)
            i += 1
        return result