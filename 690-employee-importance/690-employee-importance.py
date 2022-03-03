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
        self.result = 0
        d = {}
        for employee in employees:
            d[employee.id] = employee
            
        
        
        def dfs(l):
            self.result += l.importance
            if len(l.subordinates) == 0:
                return
            
            for i in range(len(l.subordinates)):
                dfs(d[l.subordinates[i]])
            
        # print(d)
        dfs(d[id])
        return self.result