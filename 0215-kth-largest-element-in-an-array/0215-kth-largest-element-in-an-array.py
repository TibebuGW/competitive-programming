class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def correctIndex(left, right, pivot_element_index):
            nums[pivot_element_index], nums[right] = nums[right], nums[pivot_element_index]
            
            walker = left
            for i in range(left, right):
                if nums[i] <= nums[right]:
                    nums[i], nums[walker] = nums[walker], nums[i]
                    walker += 1
            
            nums[walker], nums[right] = nums[right], nums[walker]
            return walker
        
        
        def quickSelect(left = 0, right = len(nums) - 1, target_index = len(nums) - k):
            
            
            pivot_element_index = random.randint(left, right)
            pivot_element_correct_index = correctIndex(left, right, pivot_element_index)
            
            if pivot_element_correct_index == target_index:
                return nums[pivot_element_correct_index]
            elif pivot_element_correct_index > target_index:
                return quickSelect(left, pivot_element_correct_index - 1, target_index)
            else:
                return quickSelect(pivot_element_correct_index + 1, right, target_index)
        
        return quickSelect()