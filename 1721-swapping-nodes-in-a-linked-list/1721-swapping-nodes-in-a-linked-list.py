# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        node = head
        while node:
            node = node.next
            length += 1
        # print(length)
        node1 = node2 = head
        if k <= length//2:
            rev_k = k-1
            k = length-k
        else:
            rev_k = length-k
            k -= 1
        
            
        while k:
            node1 = node1.next
            k -= 1
            if rev_k:
                node2 = node2.next
                rev_k -= 1
                
        # print(node1.val, node2.val)
        node1.val, node2.val = node2.val, node1.val
        return head
