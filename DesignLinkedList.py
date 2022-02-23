#################### trial 1 ######################
class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        
class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size():
            return -1
        if self.head == None:
            return -1
        count = 0
        node = self.head
        
        while node:
            if count == index:
                return node.val
            else:
                count += 1
                node = node.next

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        # print(self.head)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size(), val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size():
            return 
        if index == 0:
            self.addAtHead(val)
            return
        node = Node(val, None)
        count = 0
        temp = self.head
        while temp:
            if count+1 == index:
                node.next = temp.next
                temp.next = node
                break
            else:
                count += 1
                temp = temp.next
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size():
            return 
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        temp = self.head
        for i in range(index-1):
            temp = temp.next
        
        temp.next = temp.next.next
                
    def size(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
