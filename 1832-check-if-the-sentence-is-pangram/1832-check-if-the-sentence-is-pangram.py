class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = set()
        
        for char in sentence:
            s.add(char)
                
        return len(s) == 26