class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        d = defaultdict(list)
        max_length = 1
        for index, word in enumerate(words):
            d[len(word)].append(index)
            max_length = max(max_length, len(word))
        
        
        @lru_cache(None)
        def dp(cur_word_index):
            next_word_length = len(words[cur_word_index]) + 1
            
            if next_word_length == max_length + 1:
                return 1
            
            max_ = 0
            for i in d[next_word_length]:
                
                p1 = p2 = 0
                count = 0
                while p1 < len(words[cur_word_index]) and p2 < next_word_length:
                    if words[cur_word_index][p1] != words[i][p2]:
                        count += 1
                        p2 += 1
                    else:
                        p1 += 1
                        p2 += 1
                
                if p1 == p2 or p1 + 1 == p2:
                    max_ = max(max_, dp(i))
            
            return max_ + 1
        
        ans = 1
        for i in range(len(words)):
            # print(dp(i))
            ans = max(ans, dp(i))
            
        return ans