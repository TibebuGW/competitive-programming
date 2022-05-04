class Trie:
    def __init__(self):
        self.map = {"last": False}
        self.folders = []
        
    def insert(self, folder):
        cur = self.map
        for char in folder:
            if char not in cur:
                cur[char] = {"last": False}
            cur = cur[char]
            if cur["last"]:
                break
        
        if cur["last"] == False:
            cur["last"] = True
            self.folders.append("/".join(folder))
            
    
    def result(self):
        return self.folders
    
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        trie = Trie()
        for f in folder:
            trie.insert(f.split("/"))
            
        return trie.result()