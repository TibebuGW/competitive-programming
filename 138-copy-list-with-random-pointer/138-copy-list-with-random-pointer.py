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
        d = {}
        index = 0
        while node:
            temp.next = Node(node.val, None, None)
            d[node] = index
            node = node.next
            temp = temp.next
            index += 1
            
        original = original.next
        
        temp = original
        node = head
        
        while node:
            if not node.random:
                temp.random = None
            else:
                i = d[node.random]                   
                        
                temp1 = original
                while i:
                    temp1 = temp1.next
                    i -= 1
                temp.random = temp1
                
            temp = temp.next
            node = node.next
        
        return original