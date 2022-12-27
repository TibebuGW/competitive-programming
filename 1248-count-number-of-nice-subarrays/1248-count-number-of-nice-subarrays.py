class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        total_odds = 0
        first_odd_number = 0
        l = 0
        
        for r in range(len(nums)):
            if nums[r]%2:
                total_odds += 1
                
            
            while total_odds > k:
                if nums[l]%2:
                    total_odds -= 1
                l += 1
            first_odd_number = l
            
            while first_odd_number < r and nums[first_odd_number]%2 == 0:
                first_odd_number += 1
            
            if total_odds == k:
                ans += first_odd_number - l + 1
        
        return ans