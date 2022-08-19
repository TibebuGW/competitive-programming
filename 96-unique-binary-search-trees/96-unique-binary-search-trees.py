class Solution:
    def numTrees(self, m: int) -> int:
        dp = {0:1, 1:1, 2:2}
        def dfs(n):
            if n in dp:
                return dp[n]
            total = 0
            for i in range(1, n+1):
                a = b = 0
                if i-1 in dp:
                    a = dp[i-1]
                else:
                    a = self.numTrees(i-1)
                    dp[i-1] = a
                
                if n-i in dp:
                    b = dp[n-i]
                else:
                    b = self.numTrees(n-i)
                    dp[n-i] = b
                    
                total += a*b
        
            return total
        
        return dfs(m)