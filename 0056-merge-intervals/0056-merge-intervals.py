class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        def overlap(first, second):
            if first[0] <= second[1] and second[0] <= first[1]:
                return True
            return False
        
        intervals.sort()
        ans = []
        for start, end in intervals:
            if ans and overlap(ans[-1], [start, end]):
                cur_start, cur_end = ans.pop()
                ans.append([min(cur_start, start), max(cur_end, end)])
            else:
                ans.append([start, end])
        
        return ans