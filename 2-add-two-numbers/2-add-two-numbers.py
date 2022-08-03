# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        length1 = 0
        length2 = 0
        toReturn1 = head1 = l1
        toReturn2 = head2 = l2
        
        while l1:
            length1 += 1
            l1 = l1.next
        while l2:
            length2 += 1
            l2 = l2.next
            
        carry = 0
        if length1 >= length2:
            while head1:
                if head2:
                    if head1.val + head2.val + carry >= 10:
                        head1.val = (head1.val + head2.val + carry)%10
                        carry = 1
                    else:
                        head1.val = head1.val + head2.val + carry
                        carry = 0
                    
                    head2 = head2.next
                else:
                    if head1.val + carry >= 10:
                        head1.val = (head1.val + carry)%10
                        carry = 1
                    else:
                        head1.val = head1.val + carry
                        carry = 0
                        return toReturn1
                    
                if head1.next == None and carry == 1:
                    carry = 0
                    head1.next = ListNode(1)
                
                head1 = head1.next
            
            return toReturn1
        else:
            while head2:
                if head1:
                    if head1.val + head2.val + carry >= 10:
                        head2.val = (head1.val + head2.val + carry)%10
                        carry = 1
                    else:
                        head2.val = head1.val + head2.val + carry
                        carry = 0
                    
                    head1 = head1.next
                else:
                    if head2.val + carry >= 10:
                        head2.val = (head2.val + carry)%10
                        carry = 1
                    else:
                        head2.val = head2.val + carry
                        carry = 0
                        return toReturn2
                    
                if head2.next == None and carry == 1:
                    carry = 0
                    head2.next = ListNode(1)
                
                head2 = head2.next
            
            return toReturn2
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                
                    