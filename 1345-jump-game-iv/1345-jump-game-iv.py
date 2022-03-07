from collections import deque
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # def indices(lst, item):
        #     return [i for i, x in enumerate(lst) if x == item]
        
        # array = list(set(arr))
        d = {}
        for i in range(len(arr)):
            if arr[i] in d:
                d[arr[i]].append(i)
            else:
                d[arr[i]] = [i]
            # d[array[i]] = indices(arr, array[i])
        
        
        
        # print(d)
            
        queue = deque([(arr[0],0)])
        count = -1
        visited = set()
        visited.add(0)
        
        while queue:
            count += 1
            n = len(queue)
            
            for i in range(n):
                node = queue.popleft()
                if node[1] == len(arr)-1:
                    return count
                if node[1] > 0 and node[1]-1 not in visited:
                    visited.add(node[1]-1)
                    queue.append((arr[node[1]-1], node[1]-1))
                
                if node[1] < len(arr)-1 and node[1]+1 not in visited:
                    visited.add(node[1]+1)
                    queue.append((arr[node[1]+1], node[1]+1))
                
                if node[0] in d:
                    for index in d[node[0]]:
                        if index not in visited:
                            visited.add(index)
                            queue.append((node[0], index))

                    del d[node[0]]
                    