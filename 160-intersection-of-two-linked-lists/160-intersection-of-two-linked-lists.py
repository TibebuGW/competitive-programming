# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        headA1 = headA
        headB1 = headB
        count_A = 0
        while headA:
            count_A += 1
            headA = headA.next
            
        count_B = 0
        while headB:
            count_B += 1
            headB = headB.next
        
        # print("a", count_A, "b", count_B)
        if count_A > count_B:
            diff = count_A-count_B
            for i in range(diff):
                headA1 = headA1.next
                
        elif count_B > count_A:
            diff = count_B-count_A
            # print(diff)
            for i in range(diff):
                headB1 = headB1.next
    
        while headA1 and headB1:
            if headA1 == headB1:
                return headA1
            headA1 = headA1.next
            headB1 = headB1.next
        
        return None
            