class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix = [0] + list(accumulate(nums))
        ans = float('inf')
        queue = deque()
        
        for i in range(len(prefix)):
            while queue and prefix[i] <= prefix[queue[-1]]:
                queue.pop()
            queue.append(i)
            
            while queue and prefix[queue[-1]] - prefix[queue[0]] >= k:
                ans = min(ans, queue[-1] - queue.popleft())
        return ans if ans != float('inf') else -1