class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        result = []
        d = list(Counter(words).items())
        
        print(d)
        
        freq = [(-1*y,x) for x,y in d]
        
        # print(freq)
        
        heapq.heapify(freq)
        
        # print(freq)
        for i in range(k):
            result.append(heapq.heappop(freq)[1])
            
        return result
