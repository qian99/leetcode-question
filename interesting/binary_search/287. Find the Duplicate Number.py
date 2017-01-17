class Solution(object):
    def findDuplicate(self, nums):
        m = len(nums)
        n = m - 1
        l = 1
        r = n
        while (l < r):
            midValue = (l + r) // 2
            i = 0
            count = 0
            while i < m:
                if nums[i] >= l and nums[i] <= midValue:
                    count += 1
                i += 1
            if count > midValue - l + 1:
                r = midValue
            else:
                l = midValue + 1
        return l
        