class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        best = -1
        result = []
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                best = mid
                right = mid-1
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        
        result.append(best)
        
        left = best if best != -1 else 0
        right = len(nums)-1
        best = -1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                best = mid
                left = mid+1
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        
        result.append(best)
        return result