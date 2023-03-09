class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda task: -(task[1] - task[0]))
        total = 0
        needed = 0
        for actual, minimum in tasks:
            if total < minimum:
                temp = minimum - total
                total += temp
                needed += temp
            total -= actual
        
        return needed