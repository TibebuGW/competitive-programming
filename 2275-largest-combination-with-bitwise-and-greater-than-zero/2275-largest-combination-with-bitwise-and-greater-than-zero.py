from functools import reduce
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        max_length = 0
        for i in range(len(candidates)):
            b = bin(candidates[i])[2:]
            max_length = max(max_length, len(b))
            candidates[i] = b
        
        for i in range(len(candidates)):
            if len(candidates[i]) < max_length:
                candidates[i] = "0"*(max_length-len(candidates[i]))+candidates[i]
            
        max_ = 0
        
        for i in range(max_length):
            count = 0
            for j in range(len(candidates)):
                if candidates[j][i] == "1":
                    count += 1
            
            max_ = max(count, max_)
        
        return max_
            
                