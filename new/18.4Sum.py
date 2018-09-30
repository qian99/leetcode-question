class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        def encode(values):
            return '|'.join(map(str, values))

        def two_sum(a, t):
            hash_value = {}
            hash_repeat = {}
            result = []
            for v in a:
                if hash_value.has_key(t - v):
                    encode_value = encode([t - v, v])
                    if hash_repeat.has_key(encode_value):
                        continue
                    result.append([t-v, v])
                    hash_repeat[encode_value] = True
                hash_value[v] = True
            return result

        def three_sum(a, t):
            hash_repeat = {}
            result = []
            for i, v in enumerate(a):
                if i < 2:
                    continue
                two_sum_list = two_sum(a[:i], t - v)
                for item in two_sum_list:
                    encode_value = encode(item + [v])
                    if hash_repeat.has_key(encode_value):
                        continue
                    result.append(item + [v])
                    hash_repeat[encode_value] = True
            return result

        result = []
        hash_repeat = {}   
        for i, v in enumerate(nums):
            if i < 3:
                continue
            three_sum_list = three_sum(nums[:i], target - v)
            for item in three_sum_list:
                encode_value = encode(item + [v])
                if hash_repeat.has_key(encode_value):
                    continue
                result.append(item + [v])
                hash_repeat[encode_value] = True
        return result

