class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos = 1 if nums[0] > 0 else 0
        neg = 1 if nums[0] < 0 else 0
        ans = pos
        for i in range(1, len(nums)):
            if nums[i] > 0:
                x = pos+1
                y = neg+1 if neg>0 else 0
                pos, neg = x, y
            elif nums[i] < 0:
                x = neg+1 if neg>0 else 0
                y = pos+1
                pos, neg = x, y
            else:
                pos = 0
                neg = 0
            ans = max(ans, pos)
        return ans