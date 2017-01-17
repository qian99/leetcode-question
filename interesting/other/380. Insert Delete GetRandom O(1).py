import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashTable = {}
        self.valList = []
        self.n = 0
        self.total = 0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if self.hashTable.has_key(val):
            return False
        if self.total == self.n:
            self.valList.append(val)
            self.total += 1
        else:
            self.valList[self.n] = val
        self.hashTable[val] = self.n
        self.n += 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if self.hashTable.has_key(val):
            pos = self.hashTable[val]
            del self.hashTable[val]
            self.valList[self.n - 1], self.valList[pos] = self.valList[pos] , self.valList[self.n - 1]
            if self.hashTable.has_key(self.valList[pos]):
                self.hashTable[self.valList[pos]] = pos
            self.n -= 1
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if self.n <= 0:
            return 0
        pos = random.randint(0, self.n - 1)
        return self.valList[pos]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()