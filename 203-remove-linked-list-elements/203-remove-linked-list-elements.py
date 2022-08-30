# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        root = head
        def solve(node):
            if not node:
                return None
            
            node.next = solve(node.next)
            if node.val == val:
                return node.next
            else:
                return node
            
        return solve(root)
        