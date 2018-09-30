class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        n = len(stations)
        dp = [[0 for j in xrange(n + 1)] for i in xrange(n + 1)]
        dp[0][0] = startFuel

        res_n = 0
        for i in xrange(1, n + 1):
            p = i - 1
            for j in xrange(i + 1):
                if dp[i - 1][j] >= stations[p][0]:
                    dp[i][j] = max(dp[i][j] , dp[i - 1][j])
                if dp[i - 1][j - 1] >= stations[p][0]:
                    dp[i][j] = max(dp[i][j], dp[i -1][j - 1] + stations[p][1])

        for i in xrange(n+1):
            if dp[n][i] >= target:
                return i

        if len(stations) <= 0:
            if startFuel >= target:
                return 0
            return -1
        return -1

s = Solution()
print s.minRefuelStops(100, 50, [[50, 50]])
print s.minRefuelStops(1, 1, [])
print s.minRefuelStops(100, 1, [[10, 100]])
print s.minRefuelStops(100, 10, [[10, 60], [20,30],[30,30],[60,40]])