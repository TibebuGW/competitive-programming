class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        is_palindrome = [[0]*n for _ in range(n)]
        
        for i in range(n-1, -1 , -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j-i <= 1 or is_palindrome[i+1][j-1]:
                        is_palindrome[i][j] = 1
        
        @lru_cache(None)
        def solve(start = 0, partitions = 0):
            if n-start < 3-partitions or partitions > 3:
                return False
            
            if start == n and partitions == 3:
                return True
            
            for end in range(start, n):
                if is_palindrome[start][end] and solve(end + 1, partitions + 1):
                    return True
            
            return False
        
        return solve()