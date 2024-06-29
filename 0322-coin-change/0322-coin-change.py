class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        queue = deque([amount])
        level = 1
        s = set()
        
        while queue:
            n = len(queue)
            for i in range(n):
                val = queue.popleft()
                for coin in coins:
                    cur = val - coin
                    if cur == 0:
                        return level
                    if cur > 0 and cur not in s:
                        s.add(cur)
                        queue.append(cur)
            level += 1
        return -1