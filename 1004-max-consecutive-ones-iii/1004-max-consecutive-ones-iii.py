class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        prefix = [0]
        for num in nums: prefix.append(num + prefix[-1])
        
        def allOnesInRange(l, r):
            return prefix[r + 1] - prefix[l]
        
        def binarySearch(start):
            l = start
            r = len(nums) - 1
            best = 0
            
            while l <= r:
                mid = (l + r) >> 1
                total_ones = allOnesInRange(start, mid) + k
                total_size = mid - start + 1
                if total_ones >= total_size:
                    best = total_size
                    l = mid + 1
                else:
                    r = mid - 1
            
            return best
        
        for i in range(len(nums)):
            ans = max(ans, binarySearch(i))
        
        return ans