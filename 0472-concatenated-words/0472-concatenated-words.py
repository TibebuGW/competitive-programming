class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordDict = set(words)
        
        
        def solve(index, path, s):
            if index == len(s):
                if len(path) > 1:
                    return True
            else:
                for i in range(index+1, len(s)+1):
                    possible_word = s[index:i]
                    if possible_word in wordDict:
                        path.append(possible_word)
                        if solve(i, path, s):
                            return True
                        path.pop()
                return False
        answer = []
        for word in words:
            possible = solve(0, [], word)
            if possible:
                answer.append(word)
        
        return answer