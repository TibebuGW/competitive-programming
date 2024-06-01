class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        l = r = k
        ans = nums[k]
        min_ = nums[k]
        
        while l > 0 or r < len(nums) - 1:
            left_element = nums[l - 1] if l > 0 else 0
            right_element = nums[r + 1] if r < len(nums) - 1 else 0
            
            if left_element > right_element:
                min_ = min(min_, left_element)
                l -= 1
            else:
                min_ = min(min_, right_element)
                r += 1
            ans = max(ans, min_ * (r - l + 1))
        
        return ans