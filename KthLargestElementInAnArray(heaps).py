import heapq
class Solution:
    def findKthLargest(self, num: List[int], k: int) -> int:
        nums = [-1*x for x in num]
        heapq.heapify(nums)
        result = 0
        for i in range(k):
            result = heapq.heappop(nums)
        
        return -1*result
        
            
