class Trie:

    def __init__(self):
        self.map = defaultdict(Trie)
        

    def insert(self, word: str) -> None:
        cur = self.map
        for char in word:
            if char not in cur:
                cur[char] = defaultdict(Trie)
            cur = cur[char]
        
        cur["last"] = True

    def search(self, word: str) -> bool:
        cur = self.map
        for char in word:
            if char not in cur:
                return False
            cur = cur[char]
        return "last" in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.map
        for char in prefix:
            if char not in cur:
                return False
            cur = cur[char]
        return True

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        result = []
        freq = defaultdict(int)
        obj = Trie()
        for i in range(len(words)):
            if not obj.search(words[i]):
                obj.insert(words[i])
            freq[words[i]] += 1
        
        middle = list(Counter(freq).items())
        # print(middle)
        freq = [(-1*y,x) for x,y in middle]
        
        # print(freq)
        
        heapq.heapify(freq)
        
        # print(freq)
        for i in range(k):
            result.append(heapq.heappop(freq)[1])
            
        # print(result)
        # print(result.sort())
            
        return result
        
        