class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1)])
        step = 0
        visited = set({(0, 1)})
        
        while queue:
            n = len(queue)
            
            for _ in range(n):
                pos, speed = queue.popleft()
                if pos == target:
                    return step
                
                if (pos + speed, speed*2) not in visited:
                    visited.add((pos + speed, speed*2))
                    queue.append((pos + speed, speed*2))
                if speed > 0:
                    if (pos, -1) not in visited:
                        queue.append((pos, -1))
                        visited.add((pos, -1))
                else:
                    if (pos, 1) not in visited:
                        queue.append((pos, 1))
                        visited.add((pos, 1))
        
            step += 1