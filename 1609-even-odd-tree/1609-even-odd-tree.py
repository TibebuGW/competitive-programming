# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        queue = deque([root])
        i = True
        while queue:
            n = len(queue)
            if i:
                value = 0
                for i in range(n):
                    node = queue.popleft()
                    # print(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    
                    if node.val%2 != 1 or node.val <= value:
                        # print("here")
                        return False
                    value = node.val
                
                i = False
            else:
                value = 1000000
                for i in range(n):
                    node = queue.popleft()
                    # print(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    
                    if node.val%2 != 0 or node.val >= value:
                        # print("here1")
                        return False
                    value = node.val
                
                i = True
            
            
        return True