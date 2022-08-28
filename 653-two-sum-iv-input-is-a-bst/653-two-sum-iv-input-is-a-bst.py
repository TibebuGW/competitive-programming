# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        visited = set()
        def dfs(node):
            nonlocal visited
            if not node:
                return
            
            complement = k-node.val
            if complement in visited:
                return True
            else:
                visited.add(node.val)
                return dfs(node.left) or dfs(node.right)
            
            return False
        
        return dfs(root)