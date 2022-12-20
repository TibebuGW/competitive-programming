class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        incoming = [[0,0] for i in range(n)]
        totalTime = 0
        graph = defaultdict(list)
        
        for prev, cour in relations:
            graph[prev - 1].append(cour - 1)
            incoming[cour - 1][0] += 1
            
        que = deque()
        for i in range(n):
            if incoming[i][0] == 0:
                que.append((i, time[i]))
                
        while que:
            size = len(que)
            for _ in range(size):
                curr, maxTime = que.popleft()
                totalTime = max(totalTime, maxTime)
                
                for courses in graph[curr]:
                    incoming[courses][0] -= 1
                    incoming[courses][1] = max(incoming[courses][1], maxTime)
                    if incoming[courses][0] == 0:
                        
                        que.append((courses, incoming[courses][1] + time[courses]))
       
        return totalTime