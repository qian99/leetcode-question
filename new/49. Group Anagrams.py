class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strDict = {}
        result = []
        for s in strs:
            l = list(s)
            l.sort()
            newS = "".join(l)
            if strDict.has_key(newS):
                pos = strDict[newS]
                result[pos].append(s)
            else:
                strDict[newS] = len(result)
                result.append([s])
        return result