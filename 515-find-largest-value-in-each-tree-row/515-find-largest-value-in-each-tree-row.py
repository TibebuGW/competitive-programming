# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # print(float("-inf"))
        queue = deque([root])
        result = []
        
        while queue:
            
            n = len(queue)
            biggest = float("-inf")
            
            for i in range(n):
                
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)

                    if node.val > biggest:
                        biggest = node.val
            
            result.append(biggest)
        
        result.pop()
        return result
                    
            
                
                
                