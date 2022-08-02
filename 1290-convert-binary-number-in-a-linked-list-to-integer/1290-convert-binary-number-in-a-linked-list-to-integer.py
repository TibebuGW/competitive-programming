# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        count = -1
        temp = head
        while temp:
            count += 1
            temp = temp.next
            
        ans = 0
        while head:
            ans += (2**count)*head.val
            count -= 1
            head = head.next
        
        return ans