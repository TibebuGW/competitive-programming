import heapq
class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if not self.max_heap and not self.min_heap:
            heapq.heappush(self.max_heap, -1*num)
        else:
            if num <= -1*self.max_heap[0]:
                if (len(self.max_heap)+1)-len(self.min_heap) == 2:
                    heapq.heappush(self.min_heap, -1*(heapq.heappop(self.max_heap)))
                
                heapq.heappush(self.max_heap, -1*num)
            else:
                if (len(self.min_heap)+1)-len(self.max_heap) == 2:
                    heapq.heappush(self.min_heap, num)
                    heapq.heappush(self.max_heap, -1*(heapq.heappop(self.min_heap)))
                else:
                    heapq.heappush(self.min_heap, num)
            

    def findMedian(self) -> float:
        # print("max heap:", self.max_heap)
        # print("min heap:", self.min_heap)
        if len(self.max_heap) == len(self.min_heap):
            return (-1*self.max_heap[0]+self.min_heap[0])/2
        elif len(self.max_heap) > len(self.min_heap):
            return -1*self.max_heap[0]
        else:
            return self.min_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
