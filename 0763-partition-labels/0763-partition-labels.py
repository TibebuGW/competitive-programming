class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        start = 0
        end = 0
        last_indices = {char: index for index, char in enumerate(s)}
        
        for i in range(len(s)):
            end = max(end, last_indices[s[i]])
            
            if i == end:
                ans.append(end - start + 1)
                start = i + 1
                
        return ans