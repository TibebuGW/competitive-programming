class Solution:
    def jump(self, nums: List[int]) -> int:
        
        nums[-1] = 0
        for i in range(len(nums)-2, -1, -1):
            if nums[i] == 0:
                nums[i] = float('inf')
                continue
            limit = min(nums[i]+i, len(nums)-1)
            j = i+1
            min_ = float('inf')
            while j <= limit:
                min_ = min(min_, nums[j])
                j += 1
            
            nums[i] = min_+1
        
        return nums[0]