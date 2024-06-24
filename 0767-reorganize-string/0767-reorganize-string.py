class Solution:
    def reorganizeString(self, s: str) -> str:
        d = defaultdict(int)
        for char in s:
            d[char] += 1
        
        h = []
        for key, val in d.items():
            heapq.heappush(h, (-val, key))
        
        ans = []
        
        while h:
            if len(h) >= 2:
                first_val, first_char = heapq.heappop(h)
                second_val, second_char = heapq.heappop(h)
                
                ans.append(first_char)
                ans.append(second_char)
                
                if -first_val > 1:
                    heapq.heappush(h, (first_val + 1, first_char))
                if -second_val > 1:
                    heapq.heappush(h, (second_val + 1, second_char))
            else:
                val, char = heapq.heappop(h)
                if -val > 1:
                    return ""
                else:
                    ans.append(char)
        return "".join(ans)