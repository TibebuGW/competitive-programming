class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = []
        stack = []
        d = defaultdict(lambda: -1)
        
        i = 0
        while i < len(nums):
            
            while stack and nums[i] > nums[stack[-1]]:
                d[stack.pop()] = nums[i]
                
            if stack and i in stack:
                break
                
            stack.append(i)
            
            if i == len(nums)-1:
                i = 0
            else:
                i += 1
        
        for i in range(len(nums)):
            ans.append(d[i])
        
        return ans