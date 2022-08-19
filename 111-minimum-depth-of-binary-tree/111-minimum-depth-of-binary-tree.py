# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftDepth = self.minDepth(root.left)
        if leftDepth:
            leftDepth += 1
        else:
            leftDepth = 100000000
            
        rightDepth = self.minDepth(root.right)
        if rightDepth:
            rightDepth += 1
        else:
            rightDepth = 100000000
        
        if leftDepth == rightDepth == 100000000:
            return 1
        else:
            return min(leftDepth, rightDepth)