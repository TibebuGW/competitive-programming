class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        queue = deque([beginWord])
        level = 2
        chars = [chr(97 + i) for i in range(26)]
        visited = set()
        
        while queue:
            n = len(queue)
            for _ in range(n):
                word = queue.popleft()
                for i in range(len(word)):
                    for char in chars:
                        temp_word = list(word)
                        temp_word[i] = char
                        cur = "".join(temp_word)
                        
                        if cur in wordList:
                            if cur == endWord:
                                return level

                            if cur not in visited:
                                visited.add(cur)
                                queue.append(cur)
            
            level += 1
        
        return 0