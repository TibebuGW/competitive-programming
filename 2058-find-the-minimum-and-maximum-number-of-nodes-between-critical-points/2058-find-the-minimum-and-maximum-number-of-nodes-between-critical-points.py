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
        while node.next:
            if node.val > prev.val and node.val > node.next.val or node.val < prev.val and node.val < node.next.val:
                indices.append(counter)
            node = node.next
            prev = prev.next
            counter += 1
        
        if len(indices) <= 1:
            return [-1,-1]
        max_ = indices[-1]-indices[0]
        min_ = float('inf')
        for i in range(1, len(indices)):
            if indices[i]-indices[i-1] < min_:
                min_ = indices[i]-indices[i-1]
        # self.printer(original)
        return [min_, max_]