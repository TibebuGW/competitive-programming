# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        while(head):
            nodes.append(head)
            head = head.next
            
        for i in range(1, len(nodes)):
            j = i-1
            current = nodes[i]
            while(j >= 0):
                if(current.val < nodes[j].val):
                    nodes[j+1] = nodes[j]
                    if(j==0):
                        nodes[0] = current
                        break
                else:
                    nodes[j+1] = current
                    break  
                j -= 1
                
        for i in range(len(nodes)):
            if(i==len(nodes)-1):
                nodes[i].next = None
            else:
                nodes[i].next = nodes[i+1]
            
        return nodes[0]
