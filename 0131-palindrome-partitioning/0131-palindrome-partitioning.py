class Solution:
    def isPalindrome(self, array):
        return array == array[::-1]
    
    def partition(self, s: str) -> List[List[str]]:
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
                if self.isPalindrome(cur):
                    path.append(cur)
                    backtrack(path, [], i+1)
                    path.pop()
        
        backtrack([], [], 0)
        return ans