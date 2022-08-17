class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        a = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        s = set()
        
        for word in words:
            temp = ""
            for i in range(len(word)):
                temp += a[ord(word[i])%97]
            
            s.add(temp)
        
        return len(s)