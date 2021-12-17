class MyQueue:

    stack1 = []
    stack2 = []
    popped = 0
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.popped = 0

    def push(self, x: int) -> None:
        self.stack1.append(x)
        self.stack2.append(x)

    def pop(self) -> int:
        popped = self.stack1.pop(0)
        self.stack2.pop(0)
        return popped

    def peek(self) -> int:
        return self.stack1[0]

    def empty(self) -> bool:
        return len(self.stack1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
