"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    
        
    def cloneGraph(self, root: 'Node') -> 'Node':
        d = {}
        def dfs(node = root):
            if not node:
                return None
            head = Node(node.val)
            d[node.val] = head
    
            for nei in node.neighbors:
                if nei.val not in d:
                    head.neighbors.append(dfs(nei))
                else:
                    head.neighbors.append(d[nei.val])
    
            return head
        
        return dfs()
