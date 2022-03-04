# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        result = []
        
        while queue:
            lst = []
            n = len(queue)
            
            for i in range(n):
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    lst.append(node.val)
                
            if lst:
                result.append(self.average(lst))
            # print(result)
            
        
        return result
            
    
    def average(self, lst):
        
        return sum(lst)/len(lst)