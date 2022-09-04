class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = set()
        
        def dfs(level, candidate):
            nonlocal ans
            
            if level == 0:
                ans.add(candidate)
                return
            
            if (candidate%10)-k >= 0:
                dfs(level-1, (candidate*10)+((candidate%10)-k))
            if (candidate%10)+k <= 9:
                dfs(level-1, (candidate*10)+((candidate%10)+k))
                
        
        for i in range(1,10):
            dfs(n-1, i)
            # print(i)      
        return ans