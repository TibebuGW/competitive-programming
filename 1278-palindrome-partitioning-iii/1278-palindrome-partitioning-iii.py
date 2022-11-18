class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        if k == n:
            return 0
        ans = [float('inf')]
        
        @lru_cache(None)
        def minStepsToBePalindrome(i, j):
            length = j - i + 1
            count = 0
            if length % 2:
                l = r = (i+j)//2
                while l >= i:
                    if s[l] != s[r]:
                        count += 1
                    l -= 1
                    r += 1
            else:
                l = (i+j)//2
                r = l + 1
                while l >= i:
                    if s[l] != s[r]:
                        count += 1
                    l -= 1
                    r += 1
            
            return count
        
        @lru_cache(None)
        def solve(start = 0, partitions = 0, totalCharToChange = 0):
            if n-start < k-partitions or partitions > k:
                return            
            if start == n and partitions == k:
                ans[0] = min(ans[0], totalCharToChange)
                return
            
            for end in range(start, n):
                partitions += 1
                cur_partition_minimum = minStepsToBePalindrome(start, end)
                totalCharToChange += cur_partition_minimum
                solve(end+1, partitions, totalCharToChange)
                partitions -= 1
                totalCharToChange -= cur_partition_minimum
            
        solve()
        return ans[0]