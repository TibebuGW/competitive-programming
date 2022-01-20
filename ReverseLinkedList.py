# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        out = prev = None
        
        temp = head
        holder = []
        
        while temp:
            holder.append(temp)
            temp = temp.next
        
        # print(holder)
        if holder:
            result = ListNode(holder[-1].val)
            # print(result)
            ans = result
            for i in range(len(holder)-2, -1, -1):
                result.next = ListNode(holder[i].val)
                result = result.next
        else:
            return None
        
        return ans
            
            
