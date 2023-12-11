# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        padding = ListNode(-1, head)
        
        if not head.next:
            return head
        
        cur = head.next
        prev = head
        
        while cur:
            second = padding
            first = padding.next
            
            while first != cur and first.val <= cur.val:
                second = first
                first = first.next
                
            if first != cur:
                temp = cur.next
                second.next = cur
                cur.next = first
                prev.next = temp
                cur = prev.next
            else:
                prev = cur
                cur = cur.next
            
        return padding.next