class Solution:
    def middleware(self, arr, num):
        newarr = [math.ceil(arr[i]/num) for i in range(len(arr))]
        return sum(newarr)
        
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums.sort()
        left = 0
        right = len(nums)-1
        best = nums[-1]
        while left <= right:
            mid = (left+right)//2
            
            if nums[mid] and self.middleware(nums, nums[mid]) <= threshold:
                best = nums[mid]
                right = mid-1
            else:
                left = mid+1
                
        while best and self.middleware(nums, best) <= threshold:
            best -= 1
                
        return best+1
                
            
            
