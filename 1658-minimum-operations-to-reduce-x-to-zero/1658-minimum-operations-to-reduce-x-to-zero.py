class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        d = {0: -1}
        total = sum(nums)
        target = total - x
        cur = 0
        max_ = -1
        if target == 0:
            max_ = 0
        
        for i in range(len(nums)):
            cur += nums[i]
            if cur - target in d:
                max_ = max(max_, i - d[cur - target])
            if cur not in d:
                d[cur] = i
        
        return n - max_ if max_ != -1 else -1