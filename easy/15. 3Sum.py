class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        n = len(nums)
        i = 0
        while i < n:
            target = -nums[i]
            l = i + 1
            r = n - 1
            while l < r:
                a = nums[l]
                b = nums[r]
                if a + b == target:
                    result.append([a, b, nums[i]])
                    while l < r and nums[l] == a:
                        l += 1
                    while l < r and nums[r] == b:
                        r -= 1
                while l < r and nums[l] + nums[r] < target:
                    l += 1
                while l < r and nums[l] + nums[r] > target:
                    r -= 1
            while i < n and nums[i] == -target:
                i += 1
        return result