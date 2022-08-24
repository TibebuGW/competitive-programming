# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans = "z"*8500
        
        def dfs(node, word):
            nonlocal ans
            
            if not node:
                return
            if not node.left and not node.right:
                word += chr(97+node.val)
                ans = min(ans, word[::-1])
                
            word += chr(97+node.val)
            dfs(node.left, word)
            dfs(node.right, word)
    
        dfs(root, "")
        return ans
        