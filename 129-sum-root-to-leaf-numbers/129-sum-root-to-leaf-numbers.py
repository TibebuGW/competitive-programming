# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        
        def dfs(node, num):
            nonlocal total
            if not node:
                return
            if not node.left and not node.right:
                num = num*10 + node.val
                total += num

            num = num*10 + node.val
            dfs(node.left, num)
            dfs(node.right, num)
            
        dfs(root, 0)
        return total