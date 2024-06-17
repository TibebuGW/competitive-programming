# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        
        head1 = head
        head2 = head.next
        node1 = head1
        node2 = head2
        
        while head1.next and head1.next.next:
            head1.next = head1.next.next
            head2.next = head2.next.next
            head1 = head1.next
            head2 = head2.next
        
        head1.next = node2
        
        return node1        