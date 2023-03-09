class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        root = Trie()
        for word in words:
            cur = root
            for i in range(len(word) - 1, -1, -1):
                if word[i] not in cur.children:
                    cur.children[word[i]] = Trie()
                cur = cur.children[word[i]]
            cur.isEnd = True
        
        lengths = []
        def dfs(node = root, count = 0):
            if not node.children:
                lengths.append(count)
                return
            
            for child in node.children:
                dfs(node.children[child], count + 1)
        
        dfs()
        return sum(lengths) + len(lengths)