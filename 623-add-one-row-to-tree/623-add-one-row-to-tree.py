# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            node = TreeNode(val, root)
            return node
        
        def dfs(node, d):
            if not node:
                return
            if d == depth-1:
                left = TreeNode(val, node.left)
                right = TreeNode(val, None, node.right)
                node.left = left
                node.right = right
            else:
                dfs(node.left, d+1)
                dfs(node.right, d+1)
        
        dfs(root, 1)
        return root