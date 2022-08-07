"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = {}
        prev = None
        node = head
        
        while node:
            if node not in d:
                d[node] = Node(node.val, node.next, node.random)
                
            if head == node:
                head = d[node]
            else:
                prev.next = d[node]
                
            if node.random:
                if node.random not in d:
                    d[node.random] = Node(node.random.val, node.random.next, node.random.random)
                
                d[node].random = d[node.random]
            
            prev = d[node]
            node = node.next
        
        return head