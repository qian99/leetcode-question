class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums) - 1
        count = 0
        while n >= 0:
            if nums[n] == val:
                del nums[n]
            else:
                count += 1
            n -= 1
        return count