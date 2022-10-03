class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        
        start = 0
        
        while start < len(colors):
            total = neededTime[start]
            end = start+1
            max_ = neededTime[start]
            while end < len(colors) and colors[end] == colors[start]:
                max_ = max(max_, neededTime[end])
                total += neededTime[end]
                end += 1
            
            if end-start > 1:
                ans += (total-max_)
                start = end
            else:
                start += 1
        
        return ans