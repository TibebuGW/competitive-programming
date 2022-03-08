# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, head: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(root):
            if not root:
                return (0,-1)


            left = dfs(root.left)
            right = dfs(root.right)
            
            # print(left)
            if left[0] == right[0]:
                return (left[0]+1, root)
            elif left[0] < right[0]:
                return (right[0]+1, right[1])
            elif right[0] < left[0]:
                return (left[0]+1, left[1])
        
        return dfs(head)[1]
        