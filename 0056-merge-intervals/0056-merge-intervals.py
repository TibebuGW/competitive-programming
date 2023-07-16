class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        
        for start, end in intervals:
            if not ans:
                ans.append([start, end])
            else:
                if start <= ans[-1][-1] <= end:
                    ans[-1][-1] = end
                elif ans[-1][-1] < start:
                    ans.append([start, end])
        
        return ans