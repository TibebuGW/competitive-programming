class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        odds = 0
        
        l = 0
        for r in range(len(nums)):
            if nums[r] % 2:
                odds += 1
                
            if odds > k:
                l = first_odd_index + 1
                odds -= 1
            if odds == k:
                first_odd_index = l
                while nums[first_odd_index] % 2 == 0:
                    first_odd_index += 1
                
                ans += first_odd_index - l + 1
                
        return ans