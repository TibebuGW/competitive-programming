class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        num = 1
        while num**2 <= n:
            squares.append(num**2)
            num += 1
        
        queue = deque([n])
        level = 0
        
        while queue:
            n = len(queue)
            for i in range(n):
                cur = queue.popleft()
                for j in range(len(squares) - 1, -1, -1):
                    num = squares[j]
                    res = cur - num
                    if res == 0:
                        return level + 1
                    if res > 0:
                        queue.append(res)
            level += 1