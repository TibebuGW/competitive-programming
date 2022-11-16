import itertools
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        d = {"2":["a", "b", "c"], "3":["d", "e", "f"], "4":["g", "h", "i"], "5":["j", "k", "l"], "6":["m", "n", "o"], "7":["p", "q", "r", "s"], "8":["t", "u", "v"], "9":["w", "x", "y", "z"]}
        
        ans = []
        
        def backtrack(path = [], index = 0):
            if len(path) == len(digits):
                ans.append("".join(path))
                return
            
            for char in d[digits[index]]:
                path.append(char)
                backtrack(path, index+1)
                path.pop()
        
        backtrack()
        return ans
            
        