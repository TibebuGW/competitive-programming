class Solution:
    def fib(self, n: int) -> int:
        memo = {0:0, 1:1}
        
        def solve(num):
            if num in memo:
                return memo[num]
            else:
                memo[num] = solve(num-1) + solve(num-2)
                return memo[num]
            
        return solve(n)