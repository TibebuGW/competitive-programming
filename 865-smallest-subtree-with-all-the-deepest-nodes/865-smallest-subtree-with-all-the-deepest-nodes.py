# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(node, level):
            if not node:
                return (-1, None)
            if not node.left and not node.right:
                return (level, node)
            
            left = dfs(node.left, level+1)
            right = dfs(node.right, level+1)
            
            if left[0] == right[0]:
                return (left[0], node)
            elif left[0] > right[0]:
                return left
            else:
                return right
        
        return dfs(root, 1)[1]