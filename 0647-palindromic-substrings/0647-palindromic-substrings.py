class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        is_palindrome = [[0]*n for _ in range(n)]
        
        for i in range(n-1, -1 , -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j-i <= 1 or is_palindrome[i+1][j-1]:
                        is_palindrome[i][j] = 1
                        
        count = 0
        
        for lst in is_palindrome:
            count += lst.count(True)
        
        return count