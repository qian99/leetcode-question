class Solution(object):
    def dfs(self, result, n , s , count, sum, len):
        if len == (n<<1) and sum == 0:
            result.append(s)
            return
        if count + 1 <= n:
            self.dfs(result, n , s + '(', count + 1, sum + 1, len + 1)
        if sum - 1 >= 0:
            self.dfs(result, n, s + ')', count , sum - 1, len + 1)
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.dfs(result, n, "", 0, 0, 0)
        return result