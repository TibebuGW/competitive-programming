class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        l = 0
        queue = deque([])
        
        for i in range(k):
            while queue and queue[-1][0] < nums[i]:
                queue.pop()
            queue.append((nums[i], i))
        
        ans.append(queue[0][0])
        
        for i in range(k, len(nums)):
            if queue and queue[0][1] == l:
                queue.popleft()
            l += 1
            
            while queue and queue[-1][0] < nums[i]:
                queue.pop()
            queue.append((nums[i], i))
            
            ans.append(queue[0][0])
        
        return ans