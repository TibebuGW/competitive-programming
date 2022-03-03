# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.result = 0
        def dfs(head, parent, grandparent):
            if not head:
                return
            
            if grandparent and grandparent.val%2==0:
                self.result += head.val
                
            dfs(head.left, head, parent)
            dfs(head.right, head, parent)
                
        
        dfs(root, None, None)
        return self.result