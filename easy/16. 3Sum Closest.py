class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        n = len(nums)
        i = 0
        while i < n:
            nowValue = nums[i]
            l = i + 1
            r = n - 1
            while l < r:
                sumValue = nums[l] + nums[r] + nums[i]
                if abs(target - sumValue) < abs(target - result):
                    result = sumValue
                    if result == target:
                        return result
                if abs(target - nums[l + 1] - nums[r] - nums[i]) < abs(target - nums[l] - nums[r - 1] - nums[i]):
                    l += 1
                else:
                    r -= 1
            while i < n and nums[i] == nowValue:
                i += 1
        return result
        