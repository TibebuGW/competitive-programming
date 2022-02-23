# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head and head.next:
            if head.next.next == None:
                temp = head
                head = temp.next
                temp.next = None
                head.next = temp
                return head
            else:
                # print(temp.val)
                temp = head
                head = temp.next
                temp.next = self.swapPairs(head.next)
                head.next = temp


        return head
        
        
        
        
