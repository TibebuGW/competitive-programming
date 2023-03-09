class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        root = Trie()
        for word in strs:
            cur = root
            if not word:
                cur.children[""] = Trie()
                continue
            for char in word:
                if char not in cur.children:
                    cur.children[char] = Trie()
                cur = cur.children[char]
            cur.isEnd = True
        
        ans = []
        cur = root
        while not cur.isEnd and len(cur.children) == 1:
            char = list(cur.children.keys())[0]
            ans.append(char)
            cur = cur.children[char]
        
        return "".join(ans)