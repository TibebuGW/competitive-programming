class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = []
        stack = []
        d = defaultdict(lambda: -1)
        
        for j in range(2):
            for i in range(len(nums)):
                while stack and nums[i] > nums[stack[-1]]:
                    d[stack.pop()] = nums[i]
                stack.append(i)
        
        for i in range(len(nums)):
            ans.append(d[i])
        
        return ans