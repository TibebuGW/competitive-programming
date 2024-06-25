class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        result = 0
        resArr = []
        q = deque()
        
        count = Counter(tasks)
        a = dict(count)
        b = [[-1*v,k] for k, v in list(a.items())]
        
        heapq.heapify(b)
        
        while b:
            i = 0
            while i < n+1:
                if b:
                    c = heapq.heappop(b)
                    resArr.append(c[1])
                    q.append(c)
                    result += 1
                    i += 1
                else:
                    result += 1
                    resArr.append("idle")
                    i += 1
            while len(q) != 0:
                x = q.popleft()
                x[0] += 1
                if x[0] < 0:
                    b.append(x)
                    
            heapq.heapify(b)
                    
        while resArr[-1] == "idle":
            resArr.pop()
        return len(resArr)