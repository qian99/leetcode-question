class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        l = 0
        r = n - 1
        result = 0
        while l <= r:
            result = max(result,min(height[l],height[r])*(r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return result



class Solution(object):
    def binarySearch(self, orderList,n , value):
        l = 0
        r = n - 1
        if orderList[r] < value:
            return -1
        result = -1
        while (l <= r):
            m = (l + r) // 2
            if orderList[m][1] >= value:
                result = orderList[m][0]
                r = m - 1
            else:
                l = m + 1
        return result
    
    
    def getOrderMaxArea(self, height):
        n = len(height)
        m = 0
        orderList = []
        maxValue = 0
        for i in range(n):
            if i == 0:
                orderList.append((0,height[0]))
                m += 1
            else:
                findPos = self.binarySearch(orderList, m ,height[i])
                if findPos >= 0:
                    maxValue = max(maxValue, (i - findPos)*height[i])
                if height[i] > orderList[m - 1][1]:
                    orderList.append( (i,height[i]))
                    m += 1
        return maxValue
    
    
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        result = self.getOrderMaxArea(height)
        height.reverse()
        result = max(result, self.getOrderMaxArea(height))
        return result