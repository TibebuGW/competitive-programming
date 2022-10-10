# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        def dfs(node, total):
            if not node:
                return total
            right_val = dfs(node.right, total)
            node.val += right_val
            left_val = dfs(node.left, node.val)
            return left_val
        
        dfs(root, 0)
        return root