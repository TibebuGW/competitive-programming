class WordDictionary:

    def __init__(self):
        self.map = {}

    def addWord(self, word: str) -> None:
        cur = self.map
        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]
        
        cur["last"] = True
        # print(self.map)
        
    def searcher(self, word, index, field) -> bool:
        if index == len(word):
            # print(field)
            return "last" in field
        if word[index] == ".":
            for key, value in field.items():
                if key != "last" and self.searcher(word, index+1, field[key]):
                    return True
        if word[index] not in field:
            return False
        return self.searcher(word, index+1, field[word[index]])

    def search(self, word: str) -> bool:
        return self.searcher(word, 0, self.map)
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)