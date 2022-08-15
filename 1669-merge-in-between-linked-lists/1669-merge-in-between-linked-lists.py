# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        node2 = list2
        original = fast = slow = list1
        
        while node2.next:
            node2 = node2.next
        
        # print(node2)
        
        diff = b-a+2
        counter = b+1
        while counter:
            if diff == 0:
                slow = slow.next
            else:
                diff -= 1
            
            fast = fast.next
            counter -= 1
        # print(slow.val)
        # print(fast.val)
        slow.next = list2
        node2.next = fast
        
        return original