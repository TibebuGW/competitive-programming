# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, l1, l2):
            h = ListNode()
            dummy = h
            while l1 and l2:    
                if l1.val < l2.val:
                    h.next = l1
                    h = h.next
                    l1 = l1.next
                else:
                    h.next = l2
                    h = h.next
                    l2 = l2.next
                    
            if not l2:
                h.next = l1
            else:
                h.next = l2
            return dummy.next
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        l = 0
        r = len(lists)-1
        mid = (l+r)//2
        first = self.mergeKLists(lists[l:mid+1])
        second = self.mergeKLists(lists[mid+1:])
        return self.merge(first, second)
                