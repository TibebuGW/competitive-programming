# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = True
        def dfs(node):
            nonlocal result
            if not node:
                return 1
            leftDepth = dfs(node.left)+1
            rightDepth = dfs(node.right)+1
            if abs(leftDepth-rightDepth) > 1:
                result = False
            return max(leftDepth, rightDepth)
        
        dfs(root)
        return result
        
        
            