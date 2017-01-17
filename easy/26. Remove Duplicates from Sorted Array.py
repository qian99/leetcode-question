class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = None
        n = len(nums) - 1
        count = 0
        while n >= 0:
            value = nums[n]
            if value != pre:
                count += 1
            else:
                del nums[n]
            pre = value
            n -= 1
        return count