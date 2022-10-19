# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        in_range = lambda row, col: 0 <= row < m and 0 <= col < n
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        row = 0
        col = 0
        index = 0
        while head:            
            matrix[row][col] = head.val
            head = head.next
            
            row_inc = directions[index][0]
            col_inc = directions[index][1]
            
            if not in_range(row+row_inc, col+col_inc) or matrix[row+row_inc][col+col_inc] != -1:
                index = (index+1)%len(directions)
                row_inc = directions[index][0]
                col_inc = directions[index][1]
            
            row += row_inc
            col += col_inc
        return matrix