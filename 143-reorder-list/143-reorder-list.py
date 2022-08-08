# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = node = head1 = head
        i = 0
        prev = None
        while node:
            i += 1
            node = node.next
        
        head2 = None
        if i%2 == 0:
            while fast:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            head2 = slow
            prev.next = None
        else:
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            head2 = slow.next
            slow.next = None
        
        prev = None
        while head2:
            temp = head2.next
            head2.next = prev
            prev = head2
            head2 = temp
        head2 = prev
        
        # print(head1)
        # print()
        # print(head2)
        
        while head1 and head2:
            temp1 = head1.next
            temp2 = head2.next
            head1.next = head2
            head2.next = temp1
            head1 = temp1
            head2 = temp2
        
            
                
        
        
        
        