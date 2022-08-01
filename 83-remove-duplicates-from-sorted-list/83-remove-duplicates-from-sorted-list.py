# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        toReturn = head
        
        while head:
            temp = head.next
            val = head.val
            while temp and temp.val == val:
                temp = temp.next
            
            head.next = temp
            head = head.next
        
        return toReturn