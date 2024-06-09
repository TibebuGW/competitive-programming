class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        min_ = float('inf')
        
        while l <= r:
            mid = (l + r) // 2
            min_ = min(min_, nums[mid])
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        
        return min_
