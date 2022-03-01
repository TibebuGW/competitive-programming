"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(head):
            res = 0 
            if head == None:
                return 0
            
            for node in head.children:
                res = max(res, dfs(node))
            
            return res+1
            
        
        return dfs(root)
                            