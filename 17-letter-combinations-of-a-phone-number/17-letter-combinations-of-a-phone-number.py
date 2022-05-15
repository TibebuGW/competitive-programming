import itertools
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        d = {"2":["a", "b", "c"], "3":["d", "e", "f"], "4":["g", "h", "i"], "5":["j", "k", "l"], "6":["m", "n", "o"], "7":["p", "q", "r", "s"], "8":["t", "u", "v"], "9":["w", "x", "y", "z"]}
        
        result = []
        i_str = ""
        
        def dfs(i, path):
            if i == len(digits):
                result.append(path)
                return
            else:
                for char in d[digits[i]]:
                    path += char
                    dfs(i+1, path)
                    path = path[:-1]
        
        
        
        for char in d[digits[0]]:
            i_str = char
            dfs(1, i_str)
            
        return result