class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-101, head)
        original = dummy 
        temp = head
        
        while temp:
            last = None
            while temp.next and temp.val == temp.next.val:
                last = temp.next
                temp.next = temp.next.next
            
            if last and last.val == dummy.next.val:
                dummy.next = temp.next
            else:
                dummy = dummy.next
                dummy.next = temp.next
            temp = temp.next
        
        return original.next