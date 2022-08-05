# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller = ListNode(-101, None)
        original = smaller
        larger = ListNode(101, None)
        original_larger = larger
        temp = head
        
        while temp:
            if temp.val < x:
                smaller.next = temp
                smaller = smaller.next
                temp = temp.next
                smaller.next = None
            else:
                larger.next = temp
                larger = larger.next
                temp = temp.next
                larger.next = None
            
        
        smaller.next = original_larger.next
        return original.next