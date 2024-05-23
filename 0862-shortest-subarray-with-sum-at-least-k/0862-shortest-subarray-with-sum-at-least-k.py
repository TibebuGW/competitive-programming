class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = n + 1
        total = nums[0]
        if total >= k:
            return 1
        
        queue = deque([(nums[0], 0)])
        
        for i in range(1, len(nums)):
            total += nums[i]
            
            if total >= k:
                ans = min(ans, i + 1)
            
            
            while queue and total - queue[0][0] >= k:
                ans = min(ans, i - queue[0][1])
                queue.popleft()
            
            while queue and queue[-1][0] >= total:
                queue.pop()
            queue.append((total, i))
            
        return -1 if ans == n + 1 else ans