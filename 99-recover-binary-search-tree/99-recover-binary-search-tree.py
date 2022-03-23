# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        result = []
        
        def dfs(node):
            if not node: return
            
            dfs(node.left)
            result.append(node)
            dfs(node.right)
            
        
        dfs(root)
        # print(result)
        s = sorted(node.val for node in result)
        
        for i in range(len(s)):
            result[i].val = s[i]