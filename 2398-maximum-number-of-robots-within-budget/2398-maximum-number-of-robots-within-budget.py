class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        ans = 0
        queue = deque([])
        total = 0
        def cost_calculator(k):
            if not len(queue):
                return 0
            return queue[0][0] + (k * total)
        
        l = 0
        r = 0
        while r < n:
            total += runningCosts[r]
            while queue and queue[-1][0] < chargeTimes[r]:
                queue.pop()
            queue.append((chargeTimes[r], r))
            
            k = r - l + 1
                
            while cost_calculator(k) > budget:
                if queue and queue[0][1] == l:
                    queue.popleft()
                
                total -= runningCosts[l]
                l += 1
                k = r - l + 1
            
            cost = cost_calculator(k)
            if cost <= budget:
                ans = max(ans, k)
            
            r += 1
        
        
        return ans