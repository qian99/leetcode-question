#不断向集合中添加数字，然后查询集合中能形成的完整的区间
#用了并查集写，大概思路就是合并区间嘛，以最小的那个数字作为跟节点就可以，再计算一下区间中的数字个数就好了
#刚开始想着复杂度应该很低，但最后写出来效果不太好，应该是因为用了字典，然后查询的时候又排了序的缘故吧

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.parent = {}
        self.size = {}

    def Find(self,a):
        if a == self.parent[a]:
            return a
        self.parent[a] = self.Find(self.parent[a])
        return self.parent[a]
    def Uion(self,a, b):
        a = self.Find(a)
        b = self.Find(b)
        if a != b:
            self.parent[b] = a
            self.size[a] += self.size[b]
            self.size[b] = 0

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        if not self.parent.has_key(val):
            self.parent[val] = val
            self.size[val] = 1
            if self.parent.has_key(val - 1):
                self.Uion(val - 1,val)
            if self.parent.has_key(val + 1):
                self.Uion(val, val + 1)

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        result = []
        for k in sorted(self.parent.keys()):
            if self.size[k] > 0:
                result.append(Interval(k, k + self.size[k] - 1))
        return result


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()