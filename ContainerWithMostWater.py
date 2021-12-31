class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxarea = 0
        
        while left < right:
            x = min(height[left], height[right])
            if x*(right-left) > maxarea:
                maxarea = x*(right-left)
            
            if x == height[left]:
                left += 1
            else:
                right -= 1
            
        
        return maxarea
