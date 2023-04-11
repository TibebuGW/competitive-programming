# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(curSum = 0, node = root):
            if not node:
                return
            if not node.left and not node.right:
                curSum += node.val
                if curSum == targetSum:
                    return True
                return
            
            
            
            left = dfs(curSum + node.val, node.left)
            right = dfs(curSum + node.val, node.right)
            return left or right
        
        return dfs()
        