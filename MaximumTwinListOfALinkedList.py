# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def revlist(self, head):
        previous = None
        node = head
        while node:
            nextnode = node.next
            node.next = previous
            previous = node
            node = nextnode
        
        return previous
    
    def pairSum(self, head: Optional[ListNode]) -> int:
        maxsum = 0
        
        slow = fast = current = head
        
        while fast and fast.next:
            current = slow
            slow = slow.next
            fast = fast.next.next
        
        current.next = None
        reversedhalf = self.revlist(slow)
        
        # print("head: ", head)
        # print("reversedhalf: ", reversedhalf)
        
        while head:
            maxsum = max(maxsum, head.val + reversedhalf.val)
            head = head.next
            reversedhalf = reversedhalf.next
        
        return maxsum
            
        
