class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)
        i = n - 1
        while (i > 0):
            if (nums[i] > nums[i - 1]):
                temp = nums[i:]
                temp.sort()
                nums[i:] = temp
                j = i
                while (j < n and nums[i - 1] >= nums[j]):
                    j += 1
                nums[i - 1], nums[j] = nums[j] , nums[i - 1]
                return
            i -= 1
        nums.sort()
        