import heapq
class Solution:
    def lastStoneWeight(self, stone: List[int]) -> int:
        stones = [-1*x for x in stone]
        print(stones)
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            if stones[0] == x:
                heapq.heappop(stones)
            else:
                temp = -1*stones[0]
                x = -1*x
                temp -= x
                stones[0] = temp
                heapq.heapify(stones)
        if stones:
            return -1*stones[0]
        else:
            return 0
