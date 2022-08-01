# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = ListNode()
        toReturn = temp
        temp.next = head
        while temp.next:
            if temp.next.val != val:
                temp = temp.next
            else:
                temp.next = temp.next.next
        
        return toReturn.next