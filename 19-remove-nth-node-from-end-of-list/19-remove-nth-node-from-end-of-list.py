# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = n
        slow = ListNode(0, head)
        fast = head
        head = slow
        
        while fast:
            if count != 0:
                count -= 1
            else:
                slow = slow.next
            
            fast = fast.next
        
        slow.next = slow.next.next
        
        return head.next