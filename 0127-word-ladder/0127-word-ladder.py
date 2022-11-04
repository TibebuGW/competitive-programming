class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque([beginWord])
        bank = set(wordList)
        level = 1
        
        while queue:
            n = len(queue)
            for i in range(n):
                word = queue.popleft()
                if word == endWord:
                    return level
                for i in range(len(word)):
                    temp = list(word)
                    for j in range(97, 123):
                        if ord(temp[i]) != j:
                            temp[i] = chr(j)
                            intermediate = "".join(temp)
                            if intermediate in bank:
                                queue.append(intermediate)
                                bank.remove(intermediate)
            level += 1
        
        return 0
                                