class Solution:
    def numSquares(self, n: int) -> int:
        arr = []
        i = 1
        square_num = 1
        while square_num <= n:
            arr.append(square_num)
            i += 1
            square_num = i ** 2
        
        queue = deque([n])
        level = 1
        
        while queue:
            length = len(queue)
            while length:
                cur = queue.popleft()

                for i in range(len(arr) - 1, -1, -1):
                    if cur - arr[i] == 0:
                        return level
                    elif cur - arr[i] >= 0:
                        queue.append(cur - arr[i])
                length -= 1
                    
            level += 1