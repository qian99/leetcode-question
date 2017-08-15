class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        maxPos = 0
        nowPos = 0
        while (nowPos < n-1):
            maxPos = max(maxPos , nowPos + nums[nowPos])
            if maxPos > nowPos:
                nowPos += 1
            else:
                return False
        return True

res = Solution()
print res.canJump([2])