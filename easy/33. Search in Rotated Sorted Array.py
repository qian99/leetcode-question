class Solution(object):
    def search(self, nums, target):
        def binarySearch(l, r):
            if l == r:
                if nums[l] == target:
                    return l
                else:
                    return -1
            m = (l + r) // 2
            if nums[l] <= nums[r]:
                if nums[m] >= target:
                    return binarySearch(l, m)
                else:
                    return binarySearch(m + 1, r)
            else:
                res1 = binarySearch(l, m)
                if res1 != -1:
                    return res1
                return binarySearch(m + 1,r)
        n = len(nums)
        return binarySearch(0,n - 1)
        