class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1:
            return 1
        
        total = 1
        last = 1
        
        r = 1
        while r < len(ratings):
            if ratings[r] < ratings[r - 1]:
                l = r - 1
                while r < len(ratings) and ratings[r] < ratings[r - 1]:
                    r += 1
                
                num = r - l
                total -= last
                if last >= num:
                    num -= 1
                    total += last + ((num*(num + 1)) // 2)
                elif last < num:
                    total += (num*(num + 1)) // 2
                last = 1
                r -= 1
            elif ratings[r] > ratings[r - 1]:
                total += (last + 1)
                last += 1
            else:
                total += 1
                last = 1
            
            r += 1
        
        return total