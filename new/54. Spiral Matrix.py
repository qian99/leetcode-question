class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        result = [matrix[0][0]]
        dir_x = [0,1,0,-1]
        dir_y = [1,0,-1,0]
        min_x,min_y = -1,-1
        max_x,max_y = m,n
        x, y ,d = 0, 0,0
        check_count = 0
        while(True):
            dx = x + dir_x[d]
            dy = y + dir_y[d]
            if dx <= min_x or dx >= max_x:
                if dir_x[d] > 0:
                    max_y -= 1
                else:
                    min_y += 1
                d += 1
                check_count += 1
            elif dy <= min_y or dy >= max_y:
                if dir_y[d] > 0:
                    min_x += 1
                else:
                    max_x -= 1
                d += 1
                check_count += 1
            else:
                check_count = 0
                result.append(matrix[dx][dy])
                x = dx
                y = dy
            d %= 4
            if check_count > 1:
                break
        return result
