# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node = root):
            if not node:
                return [0, 0] # [tilt_sum, total_sum]
            
            [left_tilt_sum, left_total_sum] = dfs(node.left)
            [right_tilt_sum, right_total_sum] = dfs(node.right)
            
            return [left_tilt_sum + right_tilt_sum + abs(left_total_sum - right_total_sum), left_total_sum + right_total_sum + node.val]
        
        return dfs()[0]