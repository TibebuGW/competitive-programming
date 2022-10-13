# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, left_bound=float('-inf'), right_bound=float('inf')):
            if not node:
                return True
            
            if left_bound < node.val < right_bound:
                left = dfs(node.left, left_bound, node.val)
                right = dfs(node.right, node.val, right_bound)
                return left and right
            else:
                return False
            
        return dfs(root)
            