class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        
        ans = 1
        border = points[0][1]
        for i in range(1, len(points)):
            start = points[i][0]
            end = points[i][1]
            if start > border:
                ans += 1
                border = end
            else:
                border = min(end, border)
        return ans