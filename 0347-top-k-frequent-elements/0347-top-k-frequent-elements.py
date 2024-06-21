class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        h = []
        for key, value in d.items():
            heapq.heappush(h, (-value, key))
        
        ans = []
        while k:
            value, key = heapq.heappop(h)
            ans.append(key)
            k -= 1
        
        return ans