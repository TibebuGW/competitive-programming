class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        is_palindrome = [[0]*n for _ in range(n)]
        
        for i in range(n-1, -1 , -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j-i <= 1 or is_palindrome[i+1][j-1]:
                        is_palindrome[i][j] = 1
        
        for i in range(1, n):
            for j in range(i, n-1):
                if is_palindrome[0][i-1] and is_palindrome[i][j] and is_palindrome[j+1][n-1]:
                    return True
        
        return False