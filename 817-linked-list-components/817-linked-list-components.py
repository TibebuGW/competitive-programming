# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        d = {}
        for num in nums:
            d[num] = num
        
        i = 0
        # print(d)
        while head:
            if head.val in d:
                # print(head.val, i)
                d[head.val] = i
            else:
                i += 1
            
            head = head.next
        
        # print(d)
        
        return len(set(d.values()))