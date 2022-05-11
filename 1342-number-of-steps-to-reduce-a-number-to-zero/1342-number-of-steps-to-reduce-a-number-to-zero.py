class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num > 0:
            if not num & 1:
                num = num >> 1
            else:
                num = num & (~1)
            count+=1
        
        return count