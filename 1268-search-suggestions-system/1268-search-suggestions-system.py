class TrieNode:
    def __init__(self):
        self.map = {}
        self.words = []
        self.count = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        cur = self.root
        for char in word:
            if char not in cur.map:
                cur.map[char] = TrieNode()
            
            cur = cur.map[char]
            cur.words.append(word)
        
        # print(self.root.words)
            
        cur.map["last"] = True
    
    def startsWith(self, word):
        cur = self.root
        for char in word:
            if char not in cur.map:
                return []
            cur = cur.map[char]
        
        return cur.words
    
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        result = []
        trie = Trie()
        products.sort()
        for product in products:
            trie.insert(product)
            
        for i in range(len(searchWord)):
            result.append(trie.startsWith(searchWord[:i+1])[:3])
        
        return result