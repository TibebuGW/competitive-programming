# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)
        left = right = 0
        def dfs(node, row, col):
            nonlocal d, left, right
            if not node:
                return
            
            d[col].append((row, node.val))
            dfs(node.left, row+1, col-1)
            dfs(node.right, row+1, col+1)
            left = min(left, col-1)
            right = max(right, col+1)
        
        dfs(root, 0, 0)
        ans = []
        for i in range(left, right+1):
            if i in d:
                temp = []
                arr = sorted(d[i], key=lambda tup: (tup[0], tup[1]))
                for row, value in arr:
                    temp.append(value)
                    
                ans.append(temp)
                
        return ans