"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def solve(self, node):
        # print(node.val)
        while node.next or node.child:
            if node.child:
                temp = node.next
                node.next = node.child
                node.child.prev = node
                lastNode = self.solve(node.child)
                node.child = None
                if temp:
                    temp.prev = lastNode
                    lastNode.next = temp
                    node = temp
            else:
                node = node.next
        return node
        
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        original = head
        if not head:
            return None
        
        node = self.solve(head)
        
        return original