class ListNode:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next
        
class MyHashSet:

    def __init__(self):
        self.list = ListNode()
        self.head = self.list

    def add(self, key: int) -> None:
        self.list.next = ListNode(key)
        self.list = self.list.next

    def remove(self, key: int) -> None:
        self.temp = self.head
        while self.temp:
            # print(self.temp.val)
            if self.temp.val == key:
                self.temp.val = -1
            self.temp = self.temp.next            

    def contains(self, key: int) -> bool:
        self.temp = self.head
        while self.temp:
            if self.temp.val == key:
                return True
            self.temp = self.temp.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)