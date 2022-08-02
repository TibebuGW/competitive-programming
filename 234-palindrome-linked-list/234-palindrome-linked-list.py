# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        
        if fast:
            slow = slow.next
            
        # print(prev)
        # print(slow)
        
        while prev:
            if prev.val != slow.val:
                return False
            slow = slow.next
            prev = prev.next
        
        return True