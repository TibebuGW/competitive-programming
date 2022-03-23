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
        self.first = None
        self.second = None
        
        self.prev = TreeNode(float('-inf'))
        
        
        
        def dfs(node):
            if not node: return
            
            dfs(node.left)
            if self.first==None and self.prev.val > node.val:
                self.first = self.prev
                
            if self.first and self.prev.val > node.val:
                self.second = node
            
            self.prev = node
            dfs(node.right)
            
        dfs(root)
        
        self.first.val, self.second.val = self.second.val, self.first.val