class Solution:
    def countArrangement(self, n: int) -> int:
        
        def backtrack(count = 1, visited = set()):
            if count == n + 1:
                return 1
            
            total = 0
            for num in range(1, n+1):
                if num not in visited:
                    if num % count == 0 or count % num == 0:
                        visited.add(num)
                        total += backtrack(count + 1, visited)
                        visited.remove(num)
            
            return total
        
        return backtrack()
