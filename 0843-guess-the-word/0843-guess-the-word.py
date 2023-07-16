# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        ruled_out = set()
        
        def pickRandom(candidates):
            return random.randint(0, len(candidates) - 1)
        
        def matcher(word1, word2):
            count = 0
            for i in range(6):
                if word1[i] == word2[i]:
                    count += 1
            return count
        
        
        while True:
            index = pickRandom(words)
            guess = master.guess(words[index])
            if guess == 6:
                return
            
            word = words[index]
            new_words_list = []
            for word1 in words:
                if matcher(word, word1) == guess:
                    new_words_list.append(word1)
            
            words = new_words_list