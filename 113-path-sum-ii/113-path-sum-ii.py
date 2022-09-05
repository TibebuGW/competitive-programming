# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        ans = []
        
        def dfs(node, total, elements):
            nonlocal ans
            if not node:
                return 
            
            if not node.left and not node.right:
                if total + node.val == targetSum:
                    elements.append(node.val)
                    ans.append(elements)
                    return
            
            dfs(node.left, total+node.val, elements + [node.val])
            dfs(node.right, total+node.val, elements + [node.val])
            
        
        dfs(root, 0, [])
        return ans
            