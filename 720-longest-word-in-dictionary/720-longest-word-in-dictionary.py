import time
class TrieNode:
    def __init__(self):
        self.map = {}
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.result = []
        self.maxLength = 0
        
    def insert(self, word):
        cur = self.root
        for char in word:
            if char not in cur.map:
                cur.map[char] = TrieNode()
            cur = cur.map[char]
        cur.map["last"] = True      
        
    def search(self, word):
        cur = self.root
        for char in word:
            if char not in cur.map:
                return False
            cur = cur.map[char]
        
        # print(type(cur.map))
        return "last" in cur.map
    
class Solution:
    def longestWord(self, words: List[str]) -> str:
        start = time.time()
        words = list(set(words))
        words.sort(key=len)
        trie = Trie()
        
        result = []
        maxLength = 0
        
        for i in range(len(words)):
            flag = True
            # if trie.search(words[i]):
            #     continue

            for j in range(len(words[i])-1):
                if not trie.search(words[i][:j+1]):
                    flag = False
                    break
            
            # print(words[i], flag) 
            if flag:
                if len(words[i]) > maxLength:
                    result = [words[i]]
                    maxLength = len(words[i])
                elif len(words[i]) == maxLength:
                    result.append(words[i])
                    
            trie.insert(words[i])
        
        # print(result)
        # end = time.time()
        # print(end-start)
        
        return "" if len(result) == 0 else sorted(result)[0]
            