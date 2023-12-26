class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_to_right_product = [1]
        right_to_left_product = [1]
        
        for i in range(len(nums)):
            left_to_right_product.append(nums[i] * left_to_right_product[-1])
        
        for i in range(len(nums) - 1, -1, -1):
            right_to_left_product.append(nums[i] * right_to_left_product[-1])
        
        ans = []
        # [1, 1, 2, 6, 24]
        # [1, 4, 12, 24, 24]
        for i in range(len(nums)):
            ans.append(left_to_right_product[i] * right_to_left_product[len(nums) - 1 - i])
            
        return ans