class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []
        best = -1
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (right+left)//2
            if target == nums[mid]:
                
                best = mid
                tempmid = best
                tempright = right
                templeft = left
                tempmid = mid
                right = mid-1
                while left <= right:
                    mid = (right+left)//2
                    if target == nums[mid]:
                        best = mid  
                        right = mid-1
                    elif target >= nums[mid]:
                        left = mid+1
                    
                        
                result.append(best)
                best = tempmid
                right = tempright
                mid = tempmid
                left = mid+1
                while left <= right:
                    mid = (right+left)//2
                    if target == nums[mid]:
                        best = mid  
                        left = mid+1
                    elif target <=nums[mid]:
                        right = mid-1
                    
                
                result.append(best)
                return result
                                     
            elif target < nums[mid]:
                right = mid-1
            else:
                left = mid+1
        
        return [-1,-1]
