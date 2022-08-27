# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        string = []
        
        def dfs(node):
            nonlocal string
            if not node:
                return
            
            string.append(str(node.val))
            
            if not node.left and not node.right:
                return
            elif not node.left and node.right:
                string.append("()")
                string.append("(")
                dfs(node.right)
                string.append(")")
            elif node.left and not node.right:
                string.append("(")
                dfs(node.left)
                string.append(")")
            else:
                string.append("(")
                dfs(node.left)
                string.append(")")
                string.append("(")
                dfs(node.right)
                string.append(")")
            
        dfs(root)
        return "".join(string)