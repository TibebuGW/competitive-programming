class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        for i, num in enumerate(nums):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        
        # print(stack)
        ans = 0
        for i in range(len(nums)-1, -1, -1):
            while stack and nums[i] >= nums[stack[-1]]:
                ans = max(ans, i-stack[-1])
                stack.pop()
        
        return ans