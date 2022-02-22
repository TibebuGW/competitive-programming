import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        d = list(Counter(nums).items())
        
        freq = [(-1*y,x) for x,y in d]
        
        # print(freq)
        
        heapq.heapify(freq)
        
        # print(freq)
        for i in range(k):
            result.append(heapq.heappop(freq)[1])
            
        return result
        
