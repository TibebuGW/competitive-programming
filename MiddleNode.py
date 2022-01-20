########################## Trial 1 #############################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = temp2 = head
        count = 0
        while temp1:
            count += 1
            temp1 = temp1.next
            
        for i in range(count//2):
            temp2 = temp2.next
            
        return temp2



########################## Better Solution ####################################


# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         first = second = head
        
#         while second and second.nexty:
#             first = first.next
#             second = second.next.next
            
#         return first
