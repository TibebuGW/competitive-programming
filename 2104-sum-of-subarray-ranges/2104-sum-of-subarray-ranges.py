class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        result = 0
        
        for i in range(len(nums)):
            mmax = nums[i]
            mmin = nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] > mmax:
                    mmax = nums[j]
                if nums[j] < mmin:
                    mmin = nums[j]
                # mmax = max(mmax, nums[j])
                # mmin = min(mmin, nums[j])
                
                # print('max',mmax)
                # print("min",mmin)
                result += mmax-mmin
                # print("result", result)
                
        
        return result   
                    
                