class Solution:
    def maxLength(self, arr: List[str]) -> int:
        bit_array = []
        
        for word in arr:
            bit_word = 1 << 27
            if len(set(word)) != len(word):
                continue
            for char in word:
                bit_word ^= (1 << (122 - ord(char)))
            bit_array.append(bit_word)
        
        @lru_cache(None)
        def dp(index = 0, mask = 1 << 27):
            if index == len(bit_array):
                count = 0
                for _ in range(26):
                    count += mask&1
                    mask >>= 1
                return count
            
            not_take = dp(index + 1, mask)
            take = 0
            temp = mask
            cur = bit_array[index]
            for _ in range(26):
                last_bit_mask = temp&1
                last_bit_cur = cur&1
                if last_bit_mask and last_bit_cur:
                    break
                temp >>= 1
                cur >>= 1
            else:
                take = dp(index + 1, (1 << 27) ^ (mask ^ bit_array[index]))
            
            return max(take, not_take)
        
        return dp()