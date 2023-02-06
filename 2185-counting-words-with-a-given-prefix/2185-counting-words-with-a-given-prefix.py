class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            flag = True
            p1 = p2 = 0
            for i in range(len(pref)):
                if i == len(word) or pref[i] != word[i]:
                    flag = False
                    break
            if flag:
                count += 1
        
        return count