# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        d = {}
        for i, node in enumerate(inorder):
            d[node] = i
        
        i = 0
        def dfs(l = 0, r = len(preorder) - 1):
            nonlocal i
            if l > r:
                return None
            
            val = preorder[i]
            node = TreeNode(val)
            i += 1
            node.left = dfs(l, d[val] - 1)
            node.right = dfs(d[val] + 1, r)
            return node
        
        return dfs()