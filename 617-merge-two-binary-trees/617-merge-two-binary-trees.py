# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node1, node2):
            
            if node1 and node2:
                node1.val += node2.val
                if dfs(node1.left, node2.left) == -1:
                    node1.left = node2.left
                if dfs(node1.right, node2.right) == -1:
                    node1.right = node2.right
            elif not node1 and node2:
                return -1

                
        if dfs(root1, root2) == -1:
            return root2
        return root1