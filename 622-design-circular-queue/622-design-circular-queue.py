class MyCircularQueue:

    def __init__(self, k: int):
        self.limit = k
        self.count = 0
        self.deque = collections.deque([])

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.deque.append(value)
            self.count += 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.deque.popleft()
            self.count -= 1
            return True
        else:
            return False

    def Front(self) -> int:
        if not self.isEmpty():
            return self.deque[0]
        else:
            return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.deque[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        return not self.count

    def isFull(self) -> bool:
        return self.count == self.limit


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()