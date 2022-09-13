class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0:0, 1:1, 2:1}
        
        def solve(m):
            if m in memo:
                return memo[m]
            
            memo[m] = solve(m-1) + solve(m-2) + solve(m-3)
            return memo[m]
        
        return solve(n)