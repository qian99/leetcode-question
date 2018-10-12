# class Solution(object):

#     def push_up(self, value_list, lazy_tag, rt):
#         value_list[rt] = min(value_list[rt << 1], value_list[rt << 1|1])
#         lazy_tag[rt] = -1

#     def push_down(self, value_list, lazy_tag, rt):
#         if lazy_tag[rt] >= 0:
#             value_list[rt << 1] = min(lazy_tag[rt], value_list[rt << 1])
#             lazy_tag[rt<<1] = lazy_tag[rt] if lazy_tag[rt << 1] == -1 else min(lazy_tag[rt<<1], lazy_tag[rt])
#             value_list[rt << 1|1] = min(lazy_tag[rt], value_list[rt << 1|1])
#             lazy_tag[rt<<1|1] = lazy_tag[rt] if lazy_tag[rt << 1|1] == -1 else min(lazy_tag[rt<<1|1], lazy_tag[rt])
#             lazy_tag[rt] = -1

#     def build_tree(self, value_list, lazy_tag, l, r, rt):
#         if l > r:
#             return
#         value_list[rt] = float('inf')
#         lazy_tag[rt] = -1
#         if l == r:
#             return
#         m = (l + r) >> 1
#         self.build_tree(value_list, lazy_tag, l, m, rt << 1)
#         self.build_tree(value_list, lazy_tag, m + 1, r, rt << 1| 1)

#     def modify(self, value_list, lazy_tag, l, r, L, R, rt, value):
#         if l > r:
#             return
#         self.push_down(value_list, lazy_tag, rt)
#         if L <= l and r <= R:
#             value_list[rt] = min(value, value_list[rt])
#             if lazy_tag[rt] == -1:
#                 lazy_tag[rt] = value
#             else:
#                 lazy_tag[rt] = min(lazy_tag[rt], value)
#             return
#         if l == r:
#             return
#         m = (l + r) >> 1
#         if m >= L:
#             self.modify(value_list, lazy_tag, l, m, L, R, rt << 1, value)
#         if m < R:
#             self.modify(value_list, lazy_tag, m + 1, r, L, R, rt << 1|1, value)
#         self.push_up(value_list, lazy_tag, rt)

#     def search(self,value_list, lazy_tag, l, r, pos, rt):
#         # print 'search, l:{}, r:{}, pos:{}, rt:{}, value:{}'.format(l, r, pos, rt, value_list[rt])
#         if l == r:
#             return value_list[rt]
#         self.push_down(value_list, lazy_tag, rt)
#         m = (l + r) >> 1
#         if m >= pos:
#             return self.search(value_list, lazy_tag, l, m, pos, rt << 1)
#         else:
#             return self.search(value_list, lazy_tag, m+1, r, pos, rt << 1| 1)


#     def jump(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         n = len(nums)
#         m = (n << 3) + 1
#         value_list = [0 for i in xrange(m)]
#         lazy_tag = [-1 for i in xrange(m)]
#         self.build_tree(value_list, lazy_tag, 0, n - 1, 1)
#         self.modify(value_list, lazy_tag, 0, n - 1, 0, 0, 1, 0)
#         for i in xrange(n):
#             now_min_step = self.search(value_list ,lazy_tag, 0, n - 1, i, 1)
#             max_pos = min(i + nums[i], n - 1)
#             # print i, now_min_step, max_pos
#             if i + 1 <= max_pos:
#                 self.modify(value_list, lazy_tag, 0, n - 1, i + 1, max_pos, 1, now_min_step + 1)
#         result = self.search(value_list, lazy_tag, 0, n - 1, n - 1, 1)
#         return result

# class Solution(object):
#     dp = None
#     visited = None

#     def solve(self, nums, pos):
#         if pos == 0:
#             return 0
#         if self.visited[pos]:
#             return self.dp[pos]
#         self.visited[pos] = True
#         now_p = pos - 1
#         while now_p >= 0:
#             if nums[now_p] + now_p >= pos:
#                 self.dp[pos] = min(self.dp[pos], self.solve(nums, now_p) + 1)
#             now_p -=1
#         return self.dp[pos]

#     def jump(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         n = len(nums)
#         self.dp = [float('inf') for i in xrange(n)]
#         self.visited = [False for i in xrange(n)]
#         return self.solve(nums, n - 1)

class Solution(object):

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return 0
        move_steps = 0
        l, r = 0, 0
        while True:
            max_value = 0
            for i in xrange(l, r+1):
                max_value = max(i + nums[i], max_value)
            move_steps += 1
            if max_value <= r or max_value >= n-1:
                return move_steps
            l = r + 1
            r = max_value

        return move_steps




# l = [7,0,9,6,9,6,1, 7,9,0,1,2,9,0,3]
# l = [25000 - i for i in range(25000)]
# l = [2,3,1,1,4]
l = [1,1]

s = Solution()
print s.jump(l)