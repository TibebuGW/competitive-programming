# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        total = 0
        carry = 0
        head = l2
        prev_l2 = None
        while l1 and l2:
            cur = l1.val + l2.val + carry
            l2.val = cur % 10
            carry = cur // 10
            prev_l2 = l2
            l1 = l1.next
            l2 = l2.next

        while l1:
            cur = l1.val + carry
            prev_l2.next = ListNode(cur % 10)
            carry = cur // 10
            prev_l2 = prev_l2.next
            l1 = l1.next
        
        while l2:
            cur = l2.val + carry
            l2.val = cur % 10
            carry = cur // 10
            l2 = l2.next
        
        if carry:
            l2 = head
            while l2.next:
                l2 = l2.next
            l2.next = ListNode(carry)
        return head