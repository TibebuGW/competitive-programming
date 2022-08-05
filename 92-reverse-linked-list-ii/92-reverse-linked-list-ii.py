# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        original = ListNode(-101, head)
        diff = right-left
        prev = None
        slow = fast = head
        count = 1
        while count != right:
            
            if count > diff:
                prev = slow
                slow = slow.next
            fast = fast.next
            count += 1
        
        forward = None
        if fast.next:
            forward = fast.next
        
        # prev.next = fast
        
        temp = slow
        fast.next = None
        
        while temp:
            # print(temp.val)
            temp1 = temp.next
            temp.next = forward
            forward = temp
            # print(forward.val)
            temp = temp1
            # print("f", forward.val)
            
        if prev:
            prev.next = forward
            return original.next
        
        return forward
        
       