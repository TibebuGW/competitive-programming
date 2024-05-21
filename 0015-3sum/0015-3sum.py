class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        i = 0
        while i < len(nums):
            
            target = -nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                current_value = nums[j] + nums[k]
                if current_value == target:
                    left_start = j
                    while j < k and nums[j] == nums[left_start]:
                        j += 1
                    left_side = [left_start, j]
                    
                    right_start = k
                    while left_start < k and nums[k] == nums[right_start]:
                        k -= 1
                    right_side = [k, right_start]
                    
                    ans.append([nums[i], nums[left_start], nums[right_start]])
                elif current_value > target:
                    k -= 1
                else:
                    j += 1
            current_start = i
            while i < len(nums) and nums[i] == nums[current_start]:
                i += 1
        
        return ans