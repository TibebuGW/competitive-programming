# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        i = 0
        def dfs(bound = float('inf')):
            nonlocal i
            
            if i == len(preorder) or preorder[i] > bound:
                return None
            
            node = TreeNode(preorder[i])
            val = preorder[i]
            i += 1
            node.left = dfs(val)
            node.right = dfs(bound)
            return node
        
        return dfs()