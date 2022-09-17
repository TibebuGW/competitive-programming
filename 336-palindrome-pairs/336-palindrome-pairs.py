class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ans = []
        def isPalindrome(str1):
            return str1 == str1[::-1]
        
        d = {word: index for index, word in enumerate(words)}
        
        for index, word in enumerate(words):
            n = len(word)
            for j in range(n+1):
                pre = word[:j]
                suf = word[j:]
                back = suf[::-1]
                forward = pre[::-1]
                if isPalindrome(pre) and back in d and back != word:
                    ans.append([d[suf[::-1]], index])
                
                if suf != "" and isPalindrome(suf) and forward in d:
                    ans.append([index, d[pre[::-1]]])
        
        return ans