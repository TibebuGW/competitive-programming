class Solution:
    def numSquares(self, n: int) -> int:
        queue = deque([n])
        squareRoot = []
        
        for i in range(1, n + 1):
            if i * i <= n:
                squareRoot.append(i * i)
        step = 1
        
        while queue:
            
            for _ in range(len(queue)):
                newNum = queue.popleft()
                for s in squareRoot:
                    if newNum - s == 0:
                        return step
                    if newNum - s > 0:
                        queue.append(newNum - s)
            step += 1 