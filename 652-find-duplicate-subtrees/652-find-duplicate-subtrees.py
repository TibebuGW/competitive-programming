# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        res = set()
        d = {}
            
        def dfs(node):
            nonlocal d
            nonlocal res
            if not node:
                return "#"
            # print("node.val:",node.val)
            temp = "-".join([str(node.val), dfs(node.left), dfs(node.right)])
            if temp not in d:
                d[temp] = 0
            elif d[temp] == 0:
                res.add(node)
                d[temp] += 1
            else:
                d[temp] += 1
            # print(d)
            return temp
            
        dfs(root)
        
        return res
            