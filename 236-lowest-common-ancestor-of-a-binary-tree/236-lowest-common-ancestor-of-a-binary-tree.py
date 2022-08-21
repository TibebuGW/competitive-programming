# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return None
                        
            if node == p or node == q:
                return node
            else:
                left = dfs(node.left)
                right = dfs(node.right)
                if not left and not right:
                    return None
                elif left and right:
                    return node
                elif left:
                    return left
                else:
                    return right
            
        
        return dfs(root)