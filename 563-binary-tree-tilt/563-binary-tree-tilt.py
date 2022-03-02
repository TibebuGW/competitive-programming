# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, head: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if root == None:
                return 0
            if root.right == root.left == None:
                return root.val
            else:
                left = dfs(root.left)
                right = dfs(root.right)
                self.result += abs(left-right)
                return root.val + left + right
        
        self.result = 0
        dfs(head)
        return self.result