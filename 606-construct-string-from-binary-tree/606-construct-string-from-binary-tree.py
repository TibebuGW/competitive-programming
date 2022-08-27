# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        string = ""
        
        def dfs(node):
            nonlocal string
            if not node:
                return
            
            string += str(node.val)
            
            if not node.left and not node.right:
                return
            elif not node.left and node.right:
                string += "()"
                string += "("
                dfs(node.right)
                string += ")"
            elif node.left and not node.right:
                string += "("
                dfs(node.left)
                string += ")"
            else:
                string += "("
                dfs(node.left)
                string += ")"
                string += "("
                dfs(node.right)
                string += ")"
            
        dfs(root)
        return string