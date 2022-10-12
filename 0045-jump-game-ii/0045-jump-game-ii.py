class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        l = 0
        r = nums[0]
        count = 1
        while r < len(nums)-1:
            count += 1
            temp = r
            r = max([nums[i]+i for i in range(l, r+1)])
            l = temp
        
        return count