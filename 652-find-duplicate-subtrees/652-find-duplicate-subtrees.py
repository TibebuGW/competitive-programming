# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def serialize(self, root):
        arr = []
        
        def dfs(node, level, side):
            nonlocal arr
            if not node:
                return
            
            component = "*"+str(level) + str(node.val) + side
            arr.append(component)
            dfs(node.left, level+1, "l")
            dfs(node.right, level+1, "r")
        
        dfs(root, 0,"r")
        
        return "".join(arr)
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        res = set()
        d = {}
        def inorder(node):
            if not(node):
                return []
            return inorder(node.left) + [str(node.val)] + inorder(node.right)
            
        def dfs(node):
            nonlocal d
            nonlocal res
            if not node:
                return
            # print("node.val:",node.val)
            temp = self.serialize(node)
            if temp not in d:
                d[temp] = 0
            elif d[temp] == 0:
                res.add(node)
                d[temp] += 1
            else:
                d[temp] += 1
            # print(d)
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        
        return res
            