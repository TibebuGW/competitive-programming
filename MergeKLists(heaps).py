# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        middleware = []
        for i in range(len(lists)):
            temp = lists[i]
            while temp:
                middleware.append(temp.val)
                temp = temp.next
            
        heapq.heapify(middleware)
        if middleware:
            runner = ListNode(heapq.heappop(middleware))
            result = runner
        
            while middleware:
                runner.next = ListNode(heapq.heappop(middleware))
                runner = runner.next

            return result
        else:
            return None
