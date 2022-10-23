class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def counter(limit):
            ans = 0
            for i in range(1, m+1):
                ans += min(limit//i, n)
            return ans
        
        left = 1
        right = n*m
        ans = 0
        
        while left <= right:
            mid = (left+right)//2
            count = counter(mid)
            #hard part right here
            if count < k:
                left = mid+1
            else:
                ans = mid
                right = mid-1
        return ans