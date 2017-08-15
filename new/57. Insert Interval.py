# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        n = len(intervals)
        if n == 0:
            return [newInterval]
        def merge(a,b):
            if b.start >= a.start and b.start <= a.end:
                a.end = max(a.end, b.end)
                return True
            elif a.start >= b.start and a.start <= b.end:
                a.start = b.start
                a.end = max(a.end,b.end)
                return True
            return False
        result = [intervals[0]]
        flag = merge(result[0], newInterval)
        pos = 0
        for i in range(1, n):
            sucessed = merge(result[pos], intervals[i])
            flag |= sucessed
            if not sucessed:
                result.append(intervals[i])
                pos += 1
            flag |= merge(result[pos], newInterval)
        if not flag:
            result.append(newInterval)
        return sorted(result, key=lambda i: i.start)