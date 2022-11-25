class Segment:
    
    def __init__(self, start = -1, end = -1, left = None, right = None):
        self.start = start
        self.end = end
        self.left = left
        self.right = right

class MyCalendar:

    def __init__(self):
        self.root = None
        
    def insert(self, start, end, node):
        status = False
        if not node:
            return (True, Segment(start, end))
        elif node.start <= start < node.end or node.start < end <= node.end:
            return (False, node)
        elif end <= node.start:
            status, node.left = self.insert(start, end, node.left)
            
        elif start >= node.end:
            status, node.right = self.insert(start, end, node.right)
        return (status, node)
            
        
    def book(self, start: int, end: int) -> bool:
        status, self.root = self.insert(start, end, self.root)
        return status

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)