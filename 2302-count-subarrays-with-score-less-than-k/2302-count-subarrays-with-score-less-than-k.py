class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        nums.append(k)
        ans = 0
        l = 0
        total = 0
        indices = 0
        last = 0
        
        for r in range(len(nums)):
            total += nums[r]
            indices += 1
            
            if total * indices >= k:
                max_size = r - l
                deductable_size = last - l
                max_subarrays = (max_size * (max_size + 1)) // 2
                deductable_subarrays = (deductable_size * (deductable_size + 1)) // 2
                ans += max_subarrays - deductable_subarrays
                
                while total * indices >= k:
                    total -= nums[l]
                    indices -= 1
                    l += 1
                
                last = r
        
        return ans