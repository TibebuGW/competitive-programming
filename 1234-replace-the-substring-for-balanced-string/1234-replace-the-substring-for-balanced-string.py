class Solution:
    def balancedString(self, s: str) -> int:
        ans = float('inf')
        count_dict = defaultdict(int)
        for char in s:
            count_dict[char] += 1
        
        needed_count = len(s)//4
        needed_dict = defaultdict(int)
        letters = ["Q", "E", "W", "R"]
        
        for letter in letters:
            if count_dict[letter] > needed_count:
                needed_dict[letter] = count_dict[letter] - needed_count
                
        if len(needed_dict) == 0:
            return 0
        
        current_dict = defaultdict(int)
        
        def isValid():
            for letter, value in needed_dict.items():
                if needed_dict[letter] > current_dict[letter]:
                    return False
            return True
        
        l = 0
        for r in range(len(s)):
            current_dict[s[r]] += 1
            while l <= r and isValid():
                ans = min(ans, r - l + 1)
                current_dict[s[l]] -= 1
                l += 1
        
        return ans