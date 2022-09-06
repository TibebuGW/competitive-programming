# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node:
            return None

        node.left = self.pruneTree(node.left)
        node.right = self.pruneTree(node.right)

        if not node.left and not node.right and not node.val:
            node = None

        return node
            
