# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        arr1 = []
        arr2 = []
        
        def inorder_dfs(node):
            nonlocal arr1
            if not node:
                return
            
            inorder_dfs(node.left)
            arr1.append(node.val)
            inorder_dfs(node.right)
            
        inorder_dfs(subRoot)
        small = arr1
        arr1 = []
        
        def dfs(node):
            nonlocal arr1
            if not node:
                return
            if node.val == subRoot.val:
                inorder_dfs(node)
                big = arr1
                if big == small:
                    return True
                else:
                    arr1 = []
                    return dfs(node.left) or dfs(node.right)
            else:
                return dfs(node.left) or dfs(node.right)
        
        if dfs(root):
            return True
        else:
            return False
        
        
