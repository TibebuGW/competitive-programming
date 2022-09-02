# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = []
        if root:
            queue = deque([root])
        
        
        ans = []
        
        while queue:
            n = len(queue)
            value = 101
            for i in range(n):
                node = queue.popleft()
                value = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            if value != 101:
                ans.append(value)
        
        return ans