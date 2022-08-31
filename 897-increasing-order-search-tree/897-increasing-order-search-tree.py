# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        def dfs(node):
            if not node:
                return ""
            dfs(node.left)
            node.left = None
            self.cur.right = node
            self.cur = node
            dfs(node.right)
        
        ans = self.cur = TreeNode()
        dfs(root)
        return ans.right