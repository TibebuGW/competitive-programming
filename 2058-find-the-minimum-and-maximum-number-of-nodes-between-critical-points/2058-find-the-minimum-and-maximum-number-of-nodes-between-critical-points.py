# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        counter = 1
        original = head
        node = head.next
        prev = head
        indices = []
        min_ = float('inf')
        while node.next:
            if node.val > prev.val and node.val > node.next.val or node.val < prev.val and node.val < node.next.val:
                indices.append(counter)
                if len(indices) >= 2:
                    min_ = min(min_, indices[-1]-indices[-2])
            node = node.next
            prev = prev.next
            counter += 1
        
        if len(indices) <= 1:
            return [-1,-1]
        max_ = indices[-1]-indices[0]
        return [min_, max_]