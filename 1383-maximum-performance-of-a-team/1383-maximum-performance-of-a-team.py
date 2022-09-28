import heapq
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        max_ = 0
        h = []
        total = 0
        for eff, s in sorted(zip(efficiency, speed), reverse=True):
            spd = s + total
            max_ = max(eff*spd, max_)
            heapq.heappush(h, s)
            total += s
            while len(h) > k-1:
                total -= heapq.heappop(h)
            
        return max_%(10**9 + 7)