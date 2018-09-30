class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        n = len(A)
        m = len(B)
        A.sort()
        for i in xrange(m):
            B[i] = (B[i], i)
        B.sort()
        result = [-1 for i in xrange(n)]
        temp = []
        a_pos = 0
        for i in xrange(m):
            while a_pos < n:
                value = A[a_pos]
                a_pos += 1
                if value > B[i][0]:
                    result[B[i][1]] = value
                    break
                else:
                    temp.append(value)
        while a_pos < n:
            temp.append(A[a_pos])
            a_pos += 1

        tmp_pos = 0
        for i in xrange(n):
            if result[i] < 0:
                result[i] = temp[tmp_pos]
                tmp_pos += 1
        return result

s = Solution()
print s.advantageCount([2,7,11,15], [1,10,4,11])
print s.advantageCount([12,24,8,32], [13,25,32,11])