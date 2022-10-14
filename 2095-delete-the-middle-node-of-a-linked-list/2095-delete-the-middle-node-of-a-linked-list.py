# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        if fast.next: #it is even 
            slow.next = slow.next.next
        else:
            if slow.next:
                slow.val = slow.next.val
                slow.next = slow.next.next
            else:
                head = None
        
        return head