# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        max_ = 0
        
        def dfs(node):
            nonlocal max_
            if not node:
                return (-1001, 0)
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left[0] == node.val:
                if node.val == right[0]:
                    max_ = max(max_, left[1]+right[1]+2)
                    return (node.val, max(right[1], left[1])+1)
                else:
                    max_ = max(max_, left[1]+1)
                    return (node.val, left[1]+1)
            else:
                if node.val == right[0]:
                    max_ = max(max_, right[1]+1)
                    return (node.val, right[1]+1)
                else:
                    return (node.val, 0)
        
        dfs(root)
        return max_