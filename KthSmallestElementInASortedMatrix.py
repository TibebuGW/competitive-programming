import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        result = []            
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                
                if len(result) < k:
                    heapq.heappush(result, -1*matrix[i][j])
                else: 
                    if -1*result[0] > matrix[i][j]:
                        heapq.heappop(result)
                        heapq.heappush(result, -1*matrix[i][j])
                
                
        
        return -1*result[0]
