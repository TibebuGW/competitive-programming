# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return
        
        d = {}
        i = 0
        node = head
        while node:
            d[i] = node
            i += 1
            node = node.next
        
        l = 0
        r = i - 1
        
        while l < r - 1:
            temp = d[l].next
            d[l].next = d[r]
            d[r].next = temp
            l += 1
            r -= 1
        
        d[r].next = None
        
        return