# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        
        middle = self.getMiddle(head)
        root = TreeNode(middle.val)
        right = middle.next
        left = head
        root.right = self.sortedListToBST(right)
        root.left = self.sortedListToBST(left)
        return root
        
    def getMiddle(self, root: Optional[ListNode]):
        slow = fast = prev = root
        count = 0
        
        while fast and fast.next:
            count += 1
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev:
            prev.next = None
        return slow