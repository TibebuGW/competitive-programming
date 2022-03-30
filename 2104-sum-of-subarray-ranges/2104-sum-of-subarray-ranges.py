class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        result = 0
        
        for i in range(len(nums)):
            mmax = mmin = nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] > mmax:
                    mmax = nums[j]
                if nums[j] < mmin:
                    mmin = nums[j]
                
                result += mmax-mmin
        
        return result   
                    
                