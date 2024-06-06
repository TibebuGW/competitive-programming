class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = []
        max_ = float('-inf')
        queue = deque()
        
        for i in range(len(nums)):
            while queue and i - queue[0] > k:
                queue.popleft()
            
            if queue:
                dp.append(max(dp[queue[0]] + nums[i], nums[i]))
            else:
                dp.append(nums[i])
            
            max_ = max(max_, dp[-1])
            
            while queue and dp[queue[-1]] < dp[-1]:
                queue.pop()
            queue.append(i)
        
        return max_