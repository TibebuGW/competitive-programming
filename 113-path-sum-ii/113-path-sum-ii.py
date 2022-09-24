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
            if not node.right and not node.left:
                if total_sum + node.val == targetSum:
                    arr.append(path+[node.val])
                    return
            
            dfs(node.left, total_sum+node.val, path+[node.val])
            dfs(node.right, total_sum+node.val, path+[node.val])
            
            return
        
        dfs(root, 0, [])
        return arr