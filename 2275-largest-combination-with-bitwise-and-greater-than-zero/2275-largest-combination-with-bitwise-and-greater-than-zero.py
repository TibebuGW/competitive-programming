from functools import reduce
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        A = candidates
        return max(sum(1 << i & a > 0 for a in A) for i in range(30))
                