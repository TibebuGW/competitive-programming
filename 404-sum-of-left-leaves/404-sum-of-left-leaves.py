# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def dfs(node, label):
            nonlocal ans
            if not node:
                return 
            
            if label == "left" and not node.left and not node.right:
                ans += node.val
                return 
            
            dfs(node.left, "left")
            dfs(node.right, "right")
            return 
        
        dfs(root, "none")
        return ans