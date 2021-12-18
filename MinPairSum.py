class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        i = 0
        j = len(nums)-1
        nums.sort()
        toCheck = []
        
        while i < j:
            toCheck.append(nums[i]+nums[j])
            i += 1
            j -= 1
            
        return max(toCheck)
