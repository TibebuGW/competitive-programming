class ListNode:
    def __init__(self, key=-1, val=0, next=None):
        self.key = key
        self.val = val
        self.next = next
class MyHashMap:

    def __init__(self):
        self.list = ListNode()
        self.head = self.list

    def put(self, key: int, value: int) -> None:
        # self.temp = self.head
        # while self.temp:
        #     if self.temp.key == key:
        #         self.temp.val = value
        #         return
        #     self.temp = self.temp.next
        
        self.list.next = ListNode(key, value)
        self.list = self.list.next
        

    def get(self, key: int) -> int:
        self.temp = self.head
        toReturn = -1
        while self.temp:
            if self.temp.key == key:
                toReturn = self.temp.val
            self.temp = self.temp.next
        
        return toReturn

    def remove(self, key: int) -> None:
        self.temp = self.head
        while self.temp:
            if self.temp.key == key:
                self.temp.key = -1
                self.temp.val = 0
            self.temp = self.temp.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)