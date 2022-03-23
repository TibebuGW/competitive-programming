class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {c:index for index, c in enumerate(s)}
        # print(d)
        result = []
        l = r = 0
        for index, c in enumerate(s):
            r = max(r, d[c])
            
            if r == index:
                result.append(r-l+1)
                l = r+1
        
        return result