class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def backtrack(opening, closing, path):
            if len(path) == 2*n:
                ans.append("".join(path))
                return
            
            if opening < n:
                backtrack(opening+1, closing, path + ["("])
            
            if closing < opening:
                backtrack(opening, closing+1, path + [")"])
            
        
        backtrack(0,0,[])
        
        return ans