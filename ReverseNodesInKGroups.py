# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp1 = head

        result = ListNode()
        ans = result

        holder = []

        while temp1:
            counter = 0
            while counter < k and temp1:
                holder.append(temp1.val)
                temp1 = temp1.next
                counter += 1

            if k == counter:
                while holder:
                    result.next = ListNode(holder.pop())
                    result = result.next
            else:
                holder.reverse()
                while holder:
                    result.next = ListNode(holder.pop())
                    result = result.next


        return ans.next
