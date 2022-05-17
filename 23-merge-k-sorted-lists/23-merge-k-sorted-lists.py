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
    
    def merge_sort(self, lists, l, r):
        if l > r:
            return None
        if l == r:
            return lists[l]
        mid = (l+r)//2
        first = self.merge_sort(lists, mid+1, r)
        second = self.merge_sort(lists, l, mid)
        return self.merge(first, second)
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.merge_sort(lists, 0, len(lists)-1)
       
                