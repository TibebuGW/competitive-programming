# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        original = head
        count = 0
        while head:
            count += 1
            head = head.next
        # print(count)
        
        k %= count
        if k == 0:
            return original
        # print(k)
        slow = fast = ListNode(-101, original)
        
        while fast.next:
            if k != 0:
                k -= 1
            else:
                slow = slow.next
            
            fast = fast.next
        
        toReturn = slow.next
        slow.next = None
        fast.next = original
        
        return toReturn