# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        ans = False
        
        def dfs(node, total):
            nonlocal ans
            if not node:
                return
            
            if not node.left and not node.right:
                if total+node.val == targetSum:
                    ans = True
            else:
                dfs(node.left, total+node.val)
                dfs(node.right, total+node.val)
        
        dfs(root, 0)
        return ans