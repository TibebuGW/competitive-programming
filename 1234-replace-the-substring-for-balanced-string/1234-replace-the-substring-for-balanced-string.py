class Solution:
    def balancedString(self, s: str) -> int:
        # find the characters to be deleted
        # put them in a dictionary along with the count of those characters that need to be deleted
        # after figuring that out it's a matter of finding the minimum window substring that contains those characters with their respective count
        target = len(s)//4
        ans = float('inf')
        
        char_counts = defaultdict(int)
        for char in s:
            char_counts[char] += 1
        
        target_dict = defaultdict(int)
        for key, value in char_counts.items():
            if value > target:
                target_dict[key] = value - target
        
        if len(target_dict) == 0:
            return 0
        
        def is_valid():
            for char in target_dict:
                if target_dict[char] > s_dict[char]:
                    return False
            return True
        
        l = 0
        s_dict = defaultdict(int)
        for r in range(len(s)):
            s_dict[s[r]] += 1
            
            while is_valid():
                ans = min(ans, r - l + 1)
                s_dict[s[l]] -= 1
                l += 1
            
            
        return ans
            