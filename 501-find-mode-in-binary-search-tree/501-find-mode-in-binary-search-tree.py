# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        max_ = 0
        cur = 0
        result = []
        prev = None
        
        def dfs(node):
            nonlocal max_
            nonlocal cur
            nonlocal result
            nonlocal prev
            
            if not node:
                return
            dfs(node.left)
            cur = cur+1 if node.val == prev else 1
            if cur > max_:
                max_ = cur
                result = [node.val]
            elif cur == max_:
                result.append(node.val)
            
            prev = node.val
            dfs(node.right)
        
        dfs(root)
        return result