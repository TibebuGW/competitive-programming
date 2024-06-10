class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1
        min_ = float('inf')
        min_index = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                min_index = i
                break
                
        if min_index == 0:
            if  not (nums[0] <= target <= nums[-1]):
                return False
            l = 0
            r = len(nums) - 1
        else:
            if not (nums[min_index] <= target <= nums[min_index - 1]):
                return False
            
            if nums[min_index] <= target <= nums[-1]:
                l = min_index
                r = len(nums) - 1
            else:
                l = 0
                r = min_index - 1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False