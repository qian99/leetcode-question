class Solution(object):
    def maxCoins(self, nums):
        nums.insert(0, 1)
        nums.append(1)
        n = len(nums)
        dp = [[0]*n for i in range(n)]
        d = 2
        while d < n:
            left = 0
            while left + d < n:
                right = left + d
                k = left + 1
                temp = 0
                while k < right:
                    temp = max(temp, dp[left][k] + nums[left]*nums[k]*nums[right] + dp[k][right])
                    k += 1
                dp[left][right] = temp
                left += 1
            d += 1
        return dp[0][n - 1]
        