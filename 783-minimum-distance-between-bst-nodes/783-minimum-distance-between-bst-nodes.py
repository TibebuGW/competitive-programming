# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        min_ = 10000000
        arr = []
        def dfs(node):
            nonlocal arr
            if not node:
                return
            
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        
        dfs(root)
        for i in range(1, len(arr)):
            min_ = min(min_, arr[i]-arr[i-1])
        return min_