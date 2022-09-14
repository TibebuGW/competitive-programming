class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1, 2:2}
        
        def solve(m):
            if m in memo:
                return memo[m]
            
            memo[m] = solve(m-1)+solve(m-2)
            return memo[m]
        
        return solve(n)