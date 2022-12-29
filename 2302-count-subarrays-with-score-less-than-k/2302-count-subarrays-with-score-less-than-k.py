class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        prefix = [0]
        for num in nums: prefix.append(num + prefix[-1])
        ans = 0
        
        def findScore(l, r):
            indices = r - l + 1
            total = prefix[r + 1] - prefix[l]
            return total * indices
        
        def binarySearch(start):
            l = start
            r = len(nums) - 1
            best = 0
            while l <= r:
                mid = (l + r) >> 1
                score = findScore(start, mid)
                if score < k:
                    best = max(best, mid - start + 1)
                    l = mid + 1
                else:
                    r = mid - 1
            
            return best
                    
        for i in range(len(nums)):
            ans += binarySearch(i)
        
        return ans