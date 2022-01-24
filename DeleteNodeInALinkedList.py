# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
#         print(node)
        while node.next:
            if node.next.next:
                node.val = node.next.val
                node = node.next
            else:
                node.val = node.next.val
                node.next = None
            
#         print(node)

###################### best solution #########################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # print(node)
        
        node.val = node.next.val
        node.next = node.next.next
            
        # print(node)
