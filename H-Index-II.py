class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 1 and citations[0] == 0:
            return 0
        left = 0
        right = len(citations)-1
        n = len(citations)
        best = 0
        
        while left <= right:
            mid = left+(right-left)//2;
            # print(n-mid)
            if citations[mid] >= n-mid:
                best = max(n-mid,best)
                right = mid-1
            else:
                left = mid+1
            # print(best)
        
        return best
