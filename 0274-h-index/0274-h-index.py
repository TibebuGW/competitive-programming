class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        
        def isValid(num):
            best = 0
            l = 0
            r = len(citations) - 1
            
            while l <= r:
                mid = (l + r) // 2
                if citations[mid] >= num:
                    best = mid
                    r = mid - 1
                else:
                    l = mid + 1
            
            return len(citations) - best >= num
        
        l = 0
        r = max(citations)
        best = 0
        while l <= r:
            mid = (l + r) // 2
            if isValid(mid):
                best = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return best