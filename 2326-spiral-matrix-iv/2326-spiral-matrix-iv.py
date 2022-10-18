# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        left = 0
        right = n-1
        top = 0
        bottom = m-1
        
        while left <= right and head:
            for i in range(left, right+1):
                if head:
                    matrix[top][i] = head.val
                    head = head.next
                else:
                    break
            top += 1
            
            for i in range(top, bottom+1):
                if head:
                    matrix[i][right] = head.val
                    head = head.next
                else:
                    break
            right -= 1
            
            for i in range(right, left-1, -1):
                if head:
                    matrix[bottom][i] = head.val
                    head = head.next
                else:
                    break
            bottom -= 1
            
            for i in range(bottom, top-1, -1):
                if head:
                    matrix[i][left] = head.val
                    head = head.next
                else:
                    break
            left += 1
        
        return matrix
                