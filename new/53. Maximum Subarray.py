class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        result = nums[0]
        lastMax = nums[0]
        for i in range(1, n):
            lastMax = max(nums[i], lastMax + nums[i])
            result = max(result, lastMax)
        return result

res = Solution()
print res.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])