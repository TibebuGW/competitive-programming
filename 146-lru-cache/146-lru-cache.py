class ListNode:
    def __init__(self, val=-1, next=None, back=None):
        self.val = val
        self.next = next
        self.back = back
        
class LRUCache:
    def printer(self, node):
        arr = []
        while node:
            arr.append(node.val)
            node = node.next
        print(arr)

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.counter = 0
        self.head = ListNode(-1) 
        self.tail = ListNode(-1)
        self.d = {}

    def get(self, key: int) -> int:
        # print("hereeeee", self.d[key].val)
        if key not in self.d:
            return -1
        else:
            if self.d[key].val == -1:
                return self.d[key].val
            else:
                value = self.d[key].val
                self.d[key].back.next = self.d[key].next
                self.d[key].next.back = self.d[key].back
                self.d[key].back = self.tail.back
                self.d[key].next = self.tail
                self.tail.back.next = self.d[key]
                self.tail.back = self.d[key]
                # self.printer(self.head)
                return value
            

    def put(self, key: int, value: int) -> None:
        if not self.head.next and not self.tail.back:
            node = ListNode(value)
            self.d[key] = node
            self.d[key].back = self.head
            self.head.next = self.d[key]
            self.d[key].next = self.tail
            self.tail.back = self.d[key]
            self.counter += 1
        else:
            if key in self.d and self.d[key].val != -1:
                self.d[key].val = value
                self.d[key].back.next = self.d[key].next
                self.d[key].next.back = self.d[key].back
                self.d[key].back = self.tail.back
                self.d[key].next = self.tail
                self.tail.back.next = self.d[key]
                self.tail.back = self.d[key]
            else:
                if self.counter < self.capacity:
                    node = ListNode(value)
                    self.d[key] = node
                    self.d[key].back = self.tail.back
                    self.d[key].back.next = self.d[key]
                    self.d[key].next = self.tail
                    self.tail.back = self.d[key]
                    self.counter += 1
                else:
                    node = ListNode(value)
                    self.d[key] = node
                    self.d[key].back = self.tail.back
                    self.d[key].back.next = self.d[key]
                    self.d[key].next = self.tail
                    self.tail.back = self.d[key]
                    node_to_delete = self.head.next
                    # print("here", self.head.next.val)
                    self.head.next.val = -1
                    # print("here", self.head.next.val)
                    self.head.next = self.head.next.next
                    self.head.next.back = self.head
                    node_to_delete.next = None
                    node_to_delete.back = None
                    
        # self.printer(self.head)
                    
                
                
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)