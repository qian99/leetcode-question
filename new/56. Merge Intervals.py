# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        def cmp(a,b):
            if a.start == b.start:
                if a.end == b.end:
                    return 0
                else:
                    return -1 if a.end < b.end else 1
            return -1 if a.start < b.start else 1
        intervals = sorted(intervals, cmp)
        n = len(intervals)
        if n == 0:
            return []
        result = [intervals[0]]
        pos = 0
        for inter in intervals:
            if inter.start <= result[pos].end:
                result[pos].end = max(inter.end,result[pos].end)
            else:
                result.append(inter)
                pos += 1
        return result