class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        answers = []
        def solve(index, path):
            if index >= len(s):
                answer = " ".join(path)
                answers.append(answer)
            else:
                for i in range(index+1, len(s)+1):
                    possible_word = s[index:i]
                    if possible_word in wordDict:
                        path.append(possible_word)
                        solve(i, path)
                        path.pop()
            
        solve(0, [])
        return answers