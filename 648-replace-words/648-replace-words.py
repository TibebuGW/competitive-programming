class Trie:

    def __init__(self):
        self.map = defaultdict(Trie)
        
    def insert(self, word):
        cur = self.map
        for char in word:
            if char not in cur:
                cur[char] = defaultdict(Trie)
            cur = cur[char]
        
        cur["last"] = True
            
    def search(self, word) -> bool:
        cur = self.map
        for char in word:
            if char not in cur:
                return False
            cur = cur[char]
        return "last" in cur
    
    def startsWith(self, word):
        toReturn = []
        cur = self.map
        for char in word:
            if char in cur:
                cur = cur[char]
                toReturn.append(char)
                if "last" in cur:
                    return toReturn
            else:
                return []
            
        
        return toReturn

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        ans = []
        for word in dictionary:
            trie.insert(word)
            
        sentence = sentence.split(" ")
        for word in sentence:
            a = trie.startsWith(word)
            if not len(a):
                ans.append(word)
            else:
                ans.append("".join(a))

        return " ".join(ans)