class Trie:
    def __init__(self):
        self.d = {}
    
    def insert(self, word):
        cur = self.d
        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]
        cur['end'] = True
            
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        
        for word in strs:
            trie.insert(word)
        
        ans = []
        cur = trie.d
        while len(cur) == 1 and 'end' not in cur:
            for key, val in cur.items():
                ans.append(key)
                cur = cur[key]
        
        return "".join(ans)