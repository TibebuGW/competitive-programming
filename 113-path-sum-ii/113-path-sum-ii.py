# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        arr = []
        
        def dfs(node, total_sum, path):
            nonlocal arr
            if not node:
                return
            
            total_sum += node.val
            path.append(node.val)
            if not node.right and not node.left:
                if total_sum == targetSum:
                    arr.append(path[::])
            
            dfs(node.left, total_sum, path)
            dfs(node.right, total_sum, path)
            path.pop()
            
            return
        
        dfs(root, 0, [])
        return arr