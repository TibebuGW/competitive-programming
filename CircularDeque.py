import collections
class MyCircularDeque:

    def __init__(self, k: int):
        self.q = collections.deque()
        self.size = k
        

    def insertFront(self, value: int) -> bool:
        if len(self.q) == self.size:
            return False
        else:
            self.q.append(value)
            print(self.q)
            return True
        

    def insertLast(self, value: int) -> bool:
        if len(self.q) == self.size:
            return False
        else:
            self.q.appendleft(value)
            print(self.q)
            return True

    def deleteFront(self) -> bool:
        if len(self.q) == 0:
            return False
        else:
            self.q.pop()
            print(self.q)
            return True

    def deleteLast(self) -> bool:
        if len(self.q) == 0:
            return False
        else:
            self.q.popleft()
            print(self.q)
            return True
        
            

    def getFront(self) -> int:
        if len(self.q) == 0:
            return -1
        y = self.q.pop()
        self.q.append(y)
        print(self.q)
        return y

    def getRear(self) -> int:
        if len(self.q) == 0:
            return -1
        x = self.q.popleft()
        self.q.appendleft(x)
        print(self.q)
        return x

    def isEmpty(self) -> bool:
        return len(self.q) == 0

    def isFull(self) -> bool:
        return len(self.q) == self.size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
