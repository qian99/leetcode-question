class Solution(object):
    def trap(self, height):
        n = len(height)
        if n < 3:
            return 0
        result = 0
        l = 0
        r = n - 1
        while (l < r):
            leftVal = height[l]
            rightVal = height[r]
            if leftVal <= rightVal:
                while l < r and leftVal >= height[l + 1]:
                    l += 1
                    result += leftVal - height[l]
                l += 1
            else:
                while l < r and rightVal >= height[r - 1]:
                    r -= 1
                    result += rightVal - height[r]
                r -= 1
        return result



class Solution(object):
    def trap(self, height):
        n = len(height)
        if n == 0:
            return 0
        stack = [(0,0)]*n
        stack[0] = (height[0], 0)
        result = top = 0
        i = 1
        while i < n:
            val = stack[top][0]
            pos = stack[top][1]
            if height[i] <= val:
                result += (i - pos - 1)*height[i]
            else:
                maxHeight = 0
                while top >= 0 and val <= height[i]:
                    result += (i - pos - 1)*(val - maxHeight)
                    maxHeight = max(maxHeight, val)
                    top -= 1
                    if top >= 0:
                        val = stack[top][0]
                        pos = stack[top][1]
                if top >= 0 and stack[top][0] > height[i]:
                    result += (i - stack[top][1] - 1)*(height[i] - maxHeight)
            top += 1
            stack[top] = (height[i], i)
            i += 1
        return result
        