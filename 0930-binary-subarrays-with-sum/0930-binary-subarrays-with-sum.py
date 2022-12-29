class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        if goal == 0:
            l = 0
            r = 0
            ans = 0
            while r < len(nums):
                r = l
                while r < len(nums) and nums[r] == 0:
                    r += 1
                
                size = 0
                size = r - l
                ans += (size*(size+1))//2
                
                l = r
                while l < len(nums) and nums[l] == 1:
                    l += 1
                
            return ans
        
        
        ans = 0
        total_ones = 0
        l = 0
        for r in range(len(nums)):
            total_ones += nums[r]
            
            while total_ones > goal:
                total_ones -= nums[l]
                l += 1
            
            first_one = l
            while first_one < r and nums[first_one] == 0:
                first_one += 1
            
            if l <= r:
                ans += (first_one - l + 1) * int(total_ones == goal)
        
        return ans