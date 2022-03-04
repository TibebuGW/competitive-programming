# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        
        while queue:
            ls = []
            n = len(queue)
            
            
            for i in range(n):
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    ls.append(node.val)
                else:
                    ls.append(node)
                
            if not self.symmetric(ls):
                return False
            
        return True
    
    def symmetric(self, lst):
        left = 0
        right = len(lst)-1
        
        while left <= right:
            if lst[left] != lst[right]:
                return False
            
            left +=1
            right -=1
            
        return True