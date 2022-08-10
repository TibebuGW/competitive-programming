# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        node = head.next
        start.next = None
        while node:
            temp_node = node.next
            iterator = start
            if node.val <= start.val:
                node.next = start
                start = node
            else:
                while iterator.next and iterator.next.val < node.val:
                    iterator = iterator.next
                if not iterator.next:
                    iterator.next = node
                    node.next = None
                else:
                    temp = iterator.next
                    iterator.next = node
                    node.next = temp
            node = temp_node
            
        return start