# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_ = 0
        
        def dfs(node):
            nonlocal max_
            if not node: 
                return -1
            
            left = dfs(node.left)+1
            right = dfs(node.right)+1
            
            max_ = max(max_, left+right)
            
            return max(left, right)
        
        dfs(root)
        return max_