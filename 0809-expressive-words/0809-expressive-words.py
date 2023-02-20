class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        total_ans = 0
        # do the preprocessing for s
        target_word = []
        l = 0
        r = 0
        while r < len(s):
            while r < len(s) and s[r] == s[l]:
                r += 1
            target_word.append((s[l], r - l))
            l = r
        
        # print(target_word)
        # do the preprocessing for every word in words
        words_preprocessing = [[] for _ in range(len(words))]
        for i, word in enumerate(words):
            l = 0
            r = 0
            while r < len(word):
                while r < len(word) and word[l] == word[r]:
                    r += 1
                words_preprocessing[i].append((word[l], r - l))
                l = r
                
        # check if every word in words satisfies 3 conditions for every character
        for i in range(len(words)):
            if len(words_preprocessing[i]) != len(target_word):
                continue
            stretchy = True
            for pointer in range(len(target_word)):
                case1 = target_word[pointer][0] != words_preprocessing[i][pointer][0]
                case2 = target_word[pointer][1] < words_preprocessing[i][pointer][1]
                case3 = (target_word[pointer][1] > words_preprocessing[i][pointer][1] and target_word[pointer][1] < 3)
                if case1 or case2 or case3:
                    stretchy = False
                    break
            
            # count the valid words
            if stretchy:
                total_ans += 1
        return total_ans