# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if not left:
                node.left = None
                
            if not right:
                node.right = None
                
            if not node.val and not left and not right:
                return 0
            else:
                return 1
            
        
        return root if dfs(root) else None