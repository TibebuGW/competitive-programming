from collections import deque
class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        def isPossible(size):
            total_runningCosts = 0
            queue_window = deque()
            
            for i in range(size):
                total_runningCosts += runningCosts[i]
                while queue_window and chargeTimes[queue_window[-1]] < chargeTimes[i]:
                    queue_window.pop()
                queue_window.append(i)
            
            max_chargeTimes = chargeTimes[queue_window[0]]
            if max_chargeTimes+(size*total_runningCosts) <= budget:
                return True
            
            l = 0
            for r in range(size, n):
                total_runningCosts -= runningCosts[l]
                if chargeTimes[queue_window[0]] == chargeTimes[l]:
                    queue_window.popleft()
                l += 1
                total_runningCosts += runningCosts[r]
                while queue_window and chargeTimes[queue_window[-1]] < chargeTimes[r]:
                    queue_window.pop()
                queue_window.append(r)
                max_chargeTimes = chargeTimes[queue_window[0]]
                if max_chargeTimes+(size*total_runningCosts) <= budget:
                    return True
            
            return False
        
        
        left = 1
        right = n
        ans = 0
        while left <= right:
            mid = (left+right)//2
            possible = isPossible(mid)
            if possible:
                ans = mid
                left = mid+1
            else:
                right = mid-1
        
        return ans