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
        if not head:
            return None
        old = head
        new = node = Node(0)
        prev = new
        while old:
            node.val = old.val
            node.next = Node(head.val)
            prev = node
            old = old.next
            node = node.next
        
        prev.next = None
        
        old = head
        node = new
        
        while old:
            
            tempOld = head
            tempNew = new
            while tempOld and tempOld != old.random:
                tempOld = tempOld.next
                tempNew = tempNew.next
            node.random = tempNew
            old = old.next
            node = node.next
        
        return new