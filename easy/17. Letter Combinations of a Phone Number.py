class Solution(object):
    def letterCombinations(self, digits):
        hashValue = {
            "0" : [" "],
            "1" : ["*"],
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r","s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y","z"],
        }
        dList = []
        for c in digits:
            dList.append(hashValue[c])
        n = len(dList)
        if n == 0:
            return []
        result = dList
        while n > 1:
            dList = result
            result = []
            i = 0
            j = 0
            while i < n and i + 1 < n:
                result.append([])
                for str1 in dList[i]:
                    for str2 in dList[i + 1]:
                        result[j].append(str1 + str2)
                j += 1
                i += 2
            if n & 1 == 1:
                result.append([])
                for str1 in dList[n - 1]:
                    result[j].append(str1)
            n = len(result)
        return result[0]
        