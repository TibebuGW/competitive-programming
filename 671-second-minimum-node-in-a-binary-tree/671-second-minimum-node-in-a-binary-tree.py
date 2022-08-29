# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        second_max = -1
        
        def dfs(node):
            nonlocal second_max
            if not node:
                return
            
            if node.left and node.right and node.left.val != node.right.val:
                if second_max == -1:
                    second_max = max(node.left.val, node.right.val)
                else:
                    second_max = min(second_max, max(node.left.val, node.right.val))
                    
            dfs(node.left)
            dfs(node.right)
                
        
        dfs(root)
        return second_max