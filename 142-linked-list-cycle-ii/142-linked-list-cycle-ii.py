# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = defaultdict(ListNode)
        
        while head:
            if head in d:
                return head
            else:
                d[head] = True
            
            head = head.next
        
        return None