class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        ans = [0]
        n = len(s)
        is_palindrome = [[0]*n for _ in range(n)]
        
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j-i <= 1 or is_palindrome[i+1][j-1]:
                        is_palindrome[i][j] = 1
                        
    
        dp = [0]*(n+1)
        
        for j in range(n):
            dp[j+1] = dp[j]
            for i in range(j+1):
                if is_palindrome[i][j] and j - i + 1 >= k:
                    dp[j+1] = max(dp[i]+1, dp[j+1])
    
        # print(dp)
        return dp[-1]