# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, first: Optional[TreeNode], second: Optional[TreeNode]) -> bool:
        
        def dfs(p = first, q = second):
            if not p and not q:
                return True
            
            if (not p and q) or (p and not q) or p.val != q.val:
                return False
            
            return dfs(p.left, q.left) and dfs(p.right, q.right)
        
        return dfs()