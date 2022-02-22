########################## trial 1 #############################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
            
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        
        while head:
            values.append(head.val)
            head = head.next
            
        print(values)
        reverse = values[::-1]
        print(reverse)
        
        for i in range(len(values)):
            if values[i] != reverse[i]:
                return False
        
        return True
    
