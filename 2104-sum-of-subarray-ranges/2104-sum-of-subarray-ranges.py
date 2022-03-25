class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        result = 0
        
        for i in range(len(nums)):
            incStack = [nums[i]]
            decStack = [nums[i]]
            for j in range(i+1, len(nums)):
                while incStack and nums[j]<incStack[-1]:
                    incStack.pop()
                
                incStack.append(nums[j])
                
                while decStack and nums[j]>decStack[-1]:
                    decStack.pop()
                
                decStack.append(nums[j])
                
                result += decStack[0]-incStack[0]
                
        
        return result