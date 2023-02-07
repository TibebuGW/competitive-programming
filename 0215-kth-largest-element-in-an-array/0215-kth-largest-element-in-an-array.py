class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_ = float('inf')
        max_ = float('-inf')
        for num in nums:
            min_ = min(min_, num)
            max_ = max(max_, num)
        
        arr = [0 for i in range(max_ - min_ + 1)]
        for num in nums:
            arr[num - min_] += 1
        
        for i in range(len(arr) - 1, -1, -1):
            if k - arr[i] <= 0:
                return min_ + i
            k -= arr[i]