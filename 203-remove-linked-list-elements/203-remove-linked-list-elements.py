# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = ListNode()
        toReturn = temp
        while head:
            if head.val != val:
                temp.next = ListNode(head.val)
                temp = temp.next
            head = head.next
        
        return toReturn.next