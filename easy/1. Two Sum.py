class Solution(object):
    def twoSum(self, nums, target):
        hashValue = {}
        for i,j in enumerate(nums):
            tempValue = target - j
            if tempValue in hashValue:
                return [hashValue[tempValue], i]
            hashValue[j] = i