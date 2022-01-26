# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and list2:
            return list2
        if not list2 and list1:
            return list1
        
        if not list1 and not list2:
            return None
        
        if list2.val <= list1.val:
            head = list2
            list2 = list2.next
        else:
            head = list1
            list1 = list1.next
            
        temp = head
        # print(temp.val)
        while list1 or list2:
            if list1 == None:
                temp.next = list2
                break
            if list2 == None:
                temp.next = list1
                break
                
            if list1.val <= list2.val:
                # print("list1", list1)
                # print("list2", list2)
                temp.next = list1
                temp = temp.next
                list1 = list1.next
            else:
                # print("list1", list1)
                # print("list2", list2)
                temp.next = list2
                temp =  temp.next
                list2 = list2.next
            # print(temp.val)
                
        
        return head
