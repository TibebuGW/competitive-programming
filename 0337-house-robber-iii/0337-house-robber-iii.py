# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return (0,0)
            
            lmax_, lprev = dfs(node.left)
            rmax_, rprev = dfs(node.right)
            
            max_ = max(node.val+lprev+ rprev, lmax_+ rmax_)
            prev = lmax_ + rmax_
            
            return (max_, prev)
        
        return dfs(root)[0]