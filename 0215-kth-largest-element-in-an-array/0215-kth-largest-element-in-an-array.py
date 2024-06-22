class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        
        for num in nums:
            heapq.heappush(h, num)
            if len(h) > k:
                heapq.heappop(h)
        ans = heapq.heappop(h)
        return ans