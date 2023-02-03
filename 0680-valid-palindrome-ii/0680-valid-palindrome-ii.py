class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPalindrome(left, right):
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        l = 0
        r = len(s) - 1
        
        while l <= r:
            if s[l] != s[r]:
                if isPalindrome(l, r - 1) or isPalindrome(l + 1, r):
                    return True
                return False
            l += 1
            r -= 1
        
        return True