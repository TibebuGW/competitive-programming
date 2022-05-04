class TrieNode:
    def __init__(self):
        self.map = {}
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.count = 0
        
    def insert(self, word):
        
        cur = self.root
        for char in word:
            if char not in cur.map:
                cur.map[char] = TrieNode()
            cur = cur.map[char]
        
        cur.map["last"] = True
        self.count += len(word)
        self.count += 1
    
    def prefix(self, word):
        cur = self.root
        for char in word:
            if char not in cur.map:
                return False
            cur = cur.map[char]
        return True
    
    def result(self):
        return self.count
        
    
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words))
        words.sort(key=len, reverse=True)
        # print(words)
        trie = Trie()
        trie.insert(words[0][::-1])
        
        for i in range(1, len(words)):
            if not trie.prefix(words[i][::-1]):
                trie.insert(words[i][::-1])
                
        return trie.result()