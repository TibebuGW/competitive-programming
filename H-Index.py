class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        j = len(citations)
        
        for i in range(0, len(citations)):
            if citations[i] >= j:
                return j
            else:
                j -= 1
            
        return j
