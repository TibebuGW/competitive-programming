class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = set()
        
        def dfs(level, candidate):
            nonlocal ans
            
            if level == 0:
                ans.add(int(candidate))
                return
            
            if int(candidate[-1])-k >= 0:
                dfs(level-1, candidate+str(int(candidate[-1])-k))
            if int(candidate[-1])+k <= 9:
                dfs(level-1, candidate+str(int(candidate[-1])+k))
                
        
        for i in range(1,10):
            dfs(n-1, str(i))
            # print(i)      
        return ans