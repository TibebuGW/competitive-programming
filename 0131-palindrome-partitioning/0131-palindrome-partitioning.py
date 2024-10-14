class Solution:
    
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        @lru_cache(None)
        def dp(index = 0):
            if index == len(s):
                return [[]]
            
            ans = []
            for i in range(index, len(s)):
                if isPalindrome(index, i):
                    next_ = dp(i + 1)
                    for lst in next_:
                        tmp = [s[index:i + 1]]
                        for pal in lst:
                            tmp.append(pal)
                        ans.append(tmp)
            return ans
        
        return dp()