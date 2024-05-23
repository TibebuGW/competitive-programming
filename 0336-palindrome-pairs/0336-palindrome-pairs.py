class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ans = []
        word_to_index = {word: index for index, word in enumerate(words)}
        def isPalindrome(word):
            return word == word[::-1]
        
        for cur_index, word in enumerate(words):
            for i in range(len(word)):
                prefix = word[:i]
                remaining_part = word[i:][::-1]
                if isPalindrome(prefix) and remaining_part in word_to_index and remaining_part != word:
                    ans.append([word_to_index[remaining_part], cur_index])
                    
                    
                suffix = word[i:]
                remaining_part = word[:i][::-1]
                if isPalindrome(suffix) and remaining_part in word_to_index and remaining_part != word:
                    ans.append([cur_index, word_to_index[remaining_part]])
                    if remaining_part == "":
                        ans.append([word_to_index[remaining_part], cur_index])
        
        return ans