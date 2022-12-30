class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        size = len(strs)
        s = []
        for i, cur_str in enumerate(strs):
            zeroes = 0
            ones = 0
            for char in cur_str:
                if char == "0":
                    zeroes += 1
                else:
                    ones += 1
            s.append([zeroes, ones])

        @lru_cache(None)
        def dp(idx = size - 1, zeroes = m, ones = n):

            if idx == 0:
                if s[idx][0] <= zeroes and s[idx][1] <= ones:
                    return 1
                return 0

            not_take = dp(idx - 1, zeroes, ones)
            take = float('-inf')
            if s[idx][0] <= zeroes and s[idx][1] <= ones:
                take = 1 + dp(idx - 1, zeroes - s[idx][0], ones - s[idx][1])
            return max(not_take, take)

        return dp()