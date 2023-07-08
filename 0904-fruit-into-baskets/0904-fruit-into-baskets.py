class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # initialize your ans variable to 0
        ans = 0
        
        # initialize l = 0
        l = 0
        
        # initialize dct = defaultdict(int)
        dct = defaultdict(int)
        
        # do a for loop to with variable r
        # inside the for loop create a while loop to decrease the window size until len(dct) > 2
        for r in range(len(fruits)):
            dct[fruits[r]] += 1
            while l < r and len(dct) > 2:
                dct[fruits[l]] -= 1
                if dct[fruits[l]] == 0:
                    del dct[fruits[l]]
                l += 1
            # update ans
            ans = max(ans, r - l + 1)
            
            
        # return ans
        return ans