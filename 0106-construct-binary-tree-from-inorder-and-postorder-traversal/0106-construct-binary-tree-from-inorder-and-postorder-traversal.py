# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        d = {}
        for i, node in enumerate(inorder):
            d[node] = i
            
        i = len(inorder) - 1
        def dfs(l = 0, r = len(inorder) - 1):
            nonlocal i
            if l > r:
                return None
            
            val = postorder[i]
            node = TreeNode(val)
            i -= 1
            node.right = dfs(d[val] + 1, r)
            node.left = dfs(l, d[val] - 1)
            return node
        
        return dfs()