class RangeModule:

    def __init__(self):
        self.intervals = []
        
    def left_binary_search(self, value):
        l = 0
        r = len(self.intervals) - 1
        best = len(self.intervals)
        
        while l <= r:
            mid = (l + r) // 2
            if self.intervals[mid][0] <= value <= self.intervals[mid][1]:
                return mid
            elif self.intervals[mid][0] > value:
                best = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return best
    
    def right_binary_search(self, value):
        l = 0
        r = len(self.intervals) - 1
        best = -1
        
        while l <= r:
            mid = (l + r) // 2
            if self.intervals[mid][0] <= value <= self.intervals[mid][1]:
                return mid
            elif value > self.intervals[mid][1]:
                best = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return best
            
    def addRange(self, left: int, right: int) -> None:
        left_interval = self.left_binary_search(left)
        right_interval = self.right_binary_search(right)
        temp = []
        middle_interval = [left, right]
        
        if left_interval != len(self.intervals):
            if self.intervals[left_interval][0] <= left <= self.intervals[left_interval][1]:
                middle_interval[0] = self.intervals[left_interval][0]
        
        if right_interval != -1:
            if self.intervals[right_interval][0] <= right <= self.intervals[right_interval][1]:
                middle_interval[1] = self.intervals[right_interval][1]
        
        
        for i in range(left_interval):
            temp.append(self.intervals[i])
        
        temp.append(middle_interval)
        
        for i in range(right_interval + 1, len(self.intervals)):
            temp.append(self.intervals[i])
        
        self.intervals = temp
        

    def queryRange(self, left: int, right: int) -> bool:
        left_interval = self.left_binary_search(left)
        if left_interval != len(self.intervals) and self.intervals[left_interval][0] <= left < self.intervals[left_interval][1]:
            return self.intervals[left_interval][1] >= right
        return False

    def removeRange(self, left: int, right: int) -> None:
        left_interval = self.left_binary_search(left)
        right_interval = self.right_binary_search(right)
        
        
        temp = []
        for i in range(left_interval):
            temp.append(self.intervals[i])
            
        if left_interval != len(self.intervals) and self.intervals[left_interval][0] <= left <= self.intervals[left_interval][1]:
            temp.append([self.intervals[left_interval][0], min(left, self.intervals[left_interval][1])])
            
        if right_interval != -1 and self.intervals[right_interval][0] <= right < self.intervals[right_interval][1]:
            temp.append([max(self.intervals[right_interval][0], right), self.intervals[right_interval][1]])
            
        for i in range(right_interval + 1, len(self.intervals)):
            temp.append(self.intervals[i])
        
        self.intervals = temp

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)