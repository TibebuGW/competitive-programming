import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        self.h = []
        heapq.heapify(self.h)
        
        for i in range(len(self.nums)):
            if len(self.h) < self.k:
                heapq.heappush(self.h, self.nums[i])
            else:
                heapq.heappushpop(self.h, self.nums[i])

    def add(self, val: int) -> int:
        if len(self.h) < self.k:
            heapq.heappush(self.h, val)
        else:
            heapq.heappushpop(self.h, val)
        
        return self.h[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
