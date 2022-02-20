# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        values = []
        stack = []
        
        while head:
            values.append(head.val)
            head = head.next
            
        result = [0 for i in range(len(values))]
        
        stack.append((values[0], 0))
        
        for i in range(1, len(values)):
            if values[i] <= stack[-1][0]:
                stack.append((values[i], i))
            else:
                while stack and values[i] > stack[-1][0]:
                    temp = stack.pop()
                    result[temp[1]] = values[i]
                stack.append((values[i], i))
                
        return result
