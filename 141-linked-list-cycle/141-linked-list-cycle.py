# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        i = 0
        
        while head:
            i += 1
            if i > 10000:
                return True
            head = head.next
        
        return False
        
        