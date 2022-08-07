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

        original = temp = Node(-100000)
        node = head
        
        while node:
            temp.next = Node(node.val, None, None)
            node = node.next
            temp = temp.next
            
        original = original.next
        
        temp = original
        node = head
        
        while node:
            if not node.random:
                temp.random = None
            else:
                node1 = head
                i = 0
                while node1 != node.random:
                    node1 = node1.next
                    i += 1                        
                        
                temp1 = original
                while i:
                    temp1 = temp1.next
                    i -= 1
                temp.random = temp1
                
            temp = temp.next
            node = node.next
        
        return original