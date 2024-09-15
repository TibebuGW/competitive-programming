"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        d = {}
        for emp in employees:
            d[emp.id] = (emp.importance, [sub for sub in emp.subordinates])
        
        def dfs(node = id):
            cur = d[node][0]
            for sub in d[node][1]:
                cur += dfs(sub)
            return cur
        
        return dfs()