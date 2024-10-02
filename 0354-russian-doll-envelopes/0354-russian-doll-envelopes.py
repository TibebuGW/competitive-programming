class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda envelope: (envelope[0], -envelope[1]))
        arr = [envelope[1] for envelope in envelopes]
        
        ans = []
        for i in range(len(arr)):
            if not ans or ans[-1] < arr[i]:
                ans.append(arr[i])
            else:
                j = bisect_left(ans, arr[i])
                ans[j] = arr[i]
        
        return len(ans)