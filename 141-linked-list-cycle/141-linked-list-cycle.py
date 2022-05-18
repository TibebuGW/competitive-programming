# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dct = defaultdict(ListNode)
        while head:
            if head in dct:
                return True
            else:
                dct[head] = True
            head = head.next
        
        return False
        
        