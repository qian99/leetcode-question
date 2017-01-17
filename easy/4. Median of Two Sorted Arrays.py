class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        p1 = p2 = 0
        n1 = len(nums1)
        n2 = len(nums2)
        val = []
        while(p1 < n1 and p2 < n2):
            if (nums1[p1] < nums2[p2]):
                val.append(nums1[p1])
                p1 += 1
            else:
                val.append(nums2[p2])
                p2 += 1
        while(p1 < n1):
            val.append(nums1[p1])
            p1 += 1
        while(p2 < n2):
            val.append(nums2[p2])
            p2 += 1
        if (n1 + n2) == 0:
            return 0
        median = (n1 + n2) // 2
        result = val[median]
        if (n1 + n2) & 1 == 0:
            result += val[median - 1]
            result /= 2.0
        return result