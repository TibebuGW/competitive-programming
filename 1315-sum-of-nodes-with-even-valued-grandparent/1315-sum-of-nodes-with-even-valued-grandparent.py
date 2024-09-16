# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        def dfs(node = root, father = 1, grandfather = 1):
            if not node:
                return 0
            
            cur_val = 0
            if grandfather % 2 == 0:
                cur_val = node.val
            
            return dfs(node.left, node.val, father) + dfs(node.right, node.val, father) + cur_val
        
        return dfs()