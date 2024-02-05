class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n = len(firstList)
        m = len(secondList)
        
        ans = []
        i = j = 0
        
        
        while i < n and j < m:
            
            start_point_max = max(firstList[i][0], secondList[j][0])
            end_point_min = min(firstList[i][1], secondList[j][1])
            
            if start_point_max <= end_point_min:
                ans.append([start_point_max, end_point_min])
            
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        
        return ans