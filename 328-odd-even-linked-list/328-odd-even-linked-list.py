# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        if not head.next:
            return head
        head1 = original1 = head
        head2 = original2 = head.next
        node = head
        counter = 0
        while node:
            counter += 1
            node = node.next
        
        if counter%2 == 0:
            while head1.next.next:
                head1.next = head1.next.next
                head2.next = head2.next.next
                head1 = head1.next
                head2 = head2.next
        else:
            while head2.next.next:
                head1.next = head1.next.next
                head2.next = head2.next.next
                head1 = head1.next
                head2 = head2.next
            head1.next = head1.next.next
            head1 = head1.next
            head2.next = None
        # print(original1)
        # print(original2)
        head1.next = original2
        return original1