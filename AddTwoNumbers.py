# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""
        while l1 is not None:
            num1 += str(l1.val)
            l1 = l1.next
        
        while l2 is not None:
            num2 += str(l2.val)
            l2 = l2.next
        
        total = int(num1[::-1]) + int(num2[::-1])
        total = str(total)[::-1]
        
        result = ListNode(int(total[0]))
        ans = result
        for i in total[1:]:
            result.next = ListNode(int(i))
            result = result.next
            
        return ans
        
