import random
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        
        def matcher(word1, word2):
            count = 0
            for i in range(len(word1)):
                if word1[i] == word2[i]:
                    count += 1
            return count
        
        while True:
            cur_word = random.choice(words)
            guess = master.guess(cur_word)
            if guess == 6:
                return

            candidates = []
            for word in words:
                if matcher(cur_word, word) == guess:
                    candidates.append(word)
            
            words = candidates