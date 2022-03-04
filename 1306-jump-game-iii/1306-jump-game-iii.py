from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        visited.add(start)
        queue = deque([start])
        in_bound = lambda index: 0 <= index < len(arr)
        
        if arr[start] == 0:
            return True
        
        while queue:
            n = len(queue)
            
            for i in range(n):
                node = queue.popleft()
                if in_bound(node+arr[node]):
                    if arr[node+arr[node]] == 0:
                        return True
                    else:
                        if node+arr[node] not in visited:
                            visited.add(node+arr[node])
                            queue.append(node+arr[node])
                
                if in_bound(node-arr[node]):
                    if arr[node-arr[node]] == 0:
                        return True
                    else:
                        if node-arr[node] not in visited:
                            visited.add(node-arr[node])
                            queue.append(node-arr[node])
        
        return False