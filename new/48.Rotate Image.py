class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        step = (n + 1) / 2
        for i in range(step):
            m = n - i*2
            for j in range(m - 1):
                x = i
                y = i + j
                preval = matrix[x][y]
                for k in range(4):
                    xx = y
                    yy = n - x - 1
                    temp = preval
                    preval = matrix[xx][yy]
                    matrix[xx][yy] = temp
                    x = xx
                    y = yy