# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return
        if head.next == None:
            return head
        if head.next.next == None:
            temp = None
            toReturn = head.next
            head.next.next = head
            head.next = temp
            return toReturn
        else:
            temp = self.swapPairs(head.next.next)
            toReturn = head.next
            head.next.next = head
            head.next = temp
            return toReturn
            
            