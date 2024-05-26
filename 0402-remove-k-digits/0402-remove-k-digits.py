class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        queue = deque([])
        for i in range(len(num)):
            while k and queue and queue[-1] > num[i]:
                queue.pop()
                k -= 1
            queue.append(num[i])
        
        while k and queue:
            queue.pop()
            k -= 1
        
        while queue and queue[0] == "0":
            queue.popleft()
        
        return "".join(queue) if queue else "0"