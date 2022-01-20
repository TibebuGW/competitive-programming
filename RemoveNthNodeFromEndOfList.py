

########################## Trial 1 ###############################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp1 = temp2 = head
        length = 0
        while temp1:
            length += 1
            temp1 = temp1.next
        
        if length-n == 0:
            head = head.next
            
        for i in range(length-n):
            if i == length-n-1:
                temp2.next = temp2.next.next
                break
            else:
                temp2 = temp2.next
                
        
        return head
      
########################## Better Solution ################################3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        preList = ListNode(0, head) #helps when the head is to be removed
        first = preList
        second = head
        
        for i in range(n):
            second = second.next
        
        while second:
            second = second.next
            first = first.next
        
        first.next = first.next.next
        
        return preList.next
   
