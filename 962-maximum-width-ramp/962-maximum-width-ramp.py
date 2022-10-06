class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        arr = [0]*len(nums)
        arr[-1] = nums[-1]
        
        for i in range(len(nums)-2, -1, -1):
            arr[i] = max(arr[i+1], nums[i])
        
        l = r = 0
        ans = 0
        
        while r < len(nums):
            
            while l < r and nums[l] > arr[r]:
                l += 1
            
            ans = max(ans, r-l)
            print(ans)
            r += 1
        
        return ans
            