class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 1
        
        def checkWindow(size):
            total = 0
            l = 0
            for i in range(size):
                total += nums[i]
            
            r = size
            if size * (nums[r - 1]) <= total + k:
                return True
            
            for r in range(size, n):
                total -= nums[l]
                total += nums[r]
                if size * (nums[r]) <= total + k:
                    return True
                l += 1
            
            return False
        
        left = 1
        right = n
        
        while left <= right:
            mid = (left + right) // 2
            possible = checkWindow(mid)
            if possible:
                ans = max(ans, mid)
                left = mid + 1
            else:
                right = mid - 1
        
        return ans