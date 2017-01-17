class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        i = n - 1
        while i >= 0:
            while nums[i] > 0 and nums[i] <= n:
                pos = nums[i] - 1
                if nums[pos] == nums[i]:
                    break
                nums[pos], nums[i] = nums[i], nums[pos]
            i -= 1
        i = 0
        while i < n:
            if nums[i] != i + 1:
                return i + 1
            i += 1
        return i + 1
        