class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # time complexity = O(N*N!) 
        ans = []
        
        def backtrack(index):
            if index == len(nums):
                ans.append(nums[:])
                return
            
            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                backtrack(index+1)
                nums[i], nums[index] = nums[index], nums[i]
            
        backtrack(0)
        return ans