class Solution:
    def counter(self, nums, lowerlimit, upperlimit):
        count = 0
        for i in range(len(nums)):
            if nums[i] > lowerlimit and nums[i] <= upperlimit:
                count += 1

        return count
                
    def findDuplicate(self, nums: List[int]) -> int:
        left = 1
        right = max(nums)
        lowerlimit = 0
        best = 0
        
        while left <= right:
            mid = (left+right)//2
            # print(self.counter(nums, lowerlimit, mid))
            
            if self.counter(nums, lowerlimit, mid) > mid-lowerlimit:
                best = mid
                right = mid-1
            else:
                lowerlimit = mid
                left = mid+1
            
        return best
            
            
        
        
