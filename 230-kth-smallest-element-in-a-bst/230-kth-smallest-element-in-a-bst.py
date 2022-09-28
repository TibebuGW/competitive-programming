# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = None
        
        def dfs(node, top):
            nonlocal ans 
            if not node:
                return 0
            
            left = dfs(node.left, top)
            
            if top+left+1 == k:
                ans = node.val
            
            right = dfs(node.right, top+left+1)
            
            return left+right+1
        
        dfs(root, 0)
        return ans