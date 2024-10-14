class Solution:
    
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        ans = []
        def backtrack(path, cur, index):
            if index == len(s):
                temp = []
                for palindrome in path:
                    temp.append("".join(palindrome))
                ans.append(temp[:])
                return
            
            for i in range(index, len(s)):
                cur.append(s[i])
                if isPalindrome(index, i):
                    path.append(cur)
                    backtrack(path, [], i+1)
                    path.pop()
        
        backtrack([], [], 0)
        return ans