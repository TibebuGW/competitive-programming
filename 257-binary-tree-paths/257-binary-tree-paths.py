# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        
        def dfs(node, path):
            nonlocal ans
            
            if not node:
                return
            
            if not node.left and not node.right:
                path += str(node.val)
                ans.append(path)
                return
            
            path += str(node.val)
            path += "->"
            dfs(node.left, path)
            dfs(node.right, path)
            
            return
        
        dfs(root, "")
        return ans