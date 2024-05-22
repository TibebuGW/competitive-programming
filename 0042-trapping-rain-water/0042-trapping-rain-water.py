class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        left_bounds = [float('-inf') for _ in range(n)]
        right_bounds = [float('-inf') for _ in range(n)]
        
        cur = float('-inf')
        for i in range(n):
            if height[i] <= cur:
                left_bounds[i] = cur
            else:
                cur = height[i]
        
        cur = float('-inf')
        for i in range(n - 1, -1, -1):
            if height[i] <= cur:
                right_bounds[i] = cur
            else:
                cur = height[i]
        
        for i in range(n):
            if right_bounds[i] != float('-inf') and left_bounds[i] != float('-inf'):
                ans += min(right_bounds[i], left_bounds[i]) - height[i]
            
        return ans