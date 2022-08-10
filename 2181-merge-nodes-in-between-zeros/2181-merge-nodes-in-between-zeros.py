# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        original = node = head.next
        
        while node:
            while node.next.val != 0:
                node.val += node.next.val
                node.next = node.next.next
            node.next = node.next.next
            node = node.next
        
        return original