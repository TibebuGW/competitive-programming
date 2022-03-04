# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        result = []
        level = 0
        while queue:
            lst = []
            n = len(queue)
            
            for i in range(n):
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    lst.append(node.val)
                    
            if level%2 == 0:
                result.append(lst)
            else:
                result.append(lst[::-1])
                    
            level += 1
        
        result.pop()
        return result