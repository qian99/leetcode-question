class Solution(object):
    def binary_search(self, positions, values, l, r, target_value):
        if values[positions[l]] >= target_value:
            return 0
        result = 0
        while l < r:
            mid = (l + r)//2
            p = positions[mid]
            if values[p] < target_value:
                l = mid + 1
                result = mid
            else:
                r = mid
        return positions[result] + 1

    def solve(self, heights):
        n = len(heights)
        if n < 1:
            return []
        stack = [None for i in range(n + 1)]
        result = [0 for i in range(n)]
        last_pos = 0
        stack[0] = 0
        result[0] = heights[0]
        max_value = heights
        for i in range(1, n):
            if heights[stack[last_pos]] < heights[i]:
                result[i] = heights[i]
            else:
                most_left_pos = self.binary_search(stack, heights,0, last_pos, heights[i])
                # print stack
                w = i - most_left_pos + 1
                # print i, most_left_pos, last_pos
                result[i] = w*heights[i]
            while last_pos >= 0 and heights[stack[last_pos]] > heights[i]:
                last_pos -= 1
            stack[last_pos + 1] = i
            last_pos += 1
        return result


    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        heights.reverse()
        right_result = self.solve(heights)
        heights.reverse()
        left_result = self.solve(heights)
        right_result.reverse()
        result = 0
        # print left_result, right_result
        for i in range(n):
            result = max(result, left_result[i] + right_result[i] - heights[i])
        return result

s = Solution()
print s.largestRectangleArea([3,6,5,7,4,8,1,0])
