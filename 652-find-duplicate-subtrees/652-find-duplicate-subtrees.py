# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        res = []
        
        hmap = {}
        
        def recurse(node, path):
            if node is None:
                return '#'
            
            path += ','.join([str(node.val), recurse(node.left, path), recurse(node.right, path)])
            
            if path in hmap:
                hmap[path] += 1
                if hmap[path] == 2:
                    res.append(node)
            else:
                hmap[path] = 1
                
            
            return path
        
        recurse(root, '')
        #print(hmap) I SUGGEST YOU PRINT THIS - TO UNDERSTAND WHAT IS HAPPENING.
        return res