class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # reverse sort the array
        # binary search on the answer
        # for each size on the binary search, check if it's possible to use the operations and return true/false
        # find the best size
        
        nums.sort(reverse = True)
        
        def possibleWindow(size):
            
            total = 0
            for i in range(size):
                total += nums[i]
            
            l = 0
            if total + k >= nums[l] * size:
                return True
            
            for r in range(size, len(nums)):
                total += nums[r]
                total -= nums[l]
                l += 1
                if total + k >= nums[l] * size:
                    return True
            
            return False
        
        l = 1
        r = len(nums)
        best = 1
        while l <= r:
            mid = (l + r)//2
            if possibleWindow(mid):
                best = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return best