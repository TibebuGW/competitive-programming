class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        result = 0
        
        for num in nums_set:
            if num-1 in nums_set:
                continue
            else:
                temp = num
                tempresult = 1
                while temp+1 in nums_set:
                    temp = temp+1
                    tempresult += 1
                result = max(result, tempresult)
        
        return result