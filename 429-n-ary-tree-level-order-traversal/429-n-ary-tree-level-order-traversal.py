"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root:
            queue = deque([root])
        else:
            queue = []
        arr = []
        while queue:
            n = len(queue)
            temp = []
            for i in range(n):
                node = queue.popleft()
                temp.append(node.val)
                
                for child in node.children:
                    if child:
                        queue.append(child)
                    
            arr.append(temp)
        
        return arr