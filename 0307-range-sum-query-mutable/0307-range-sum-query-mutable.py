class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.segment = [0]*(4*len(self.nums))
        self.buildSegment(0, 0, len(self.nums)-1)
        
    def update(self, index: int, val: int) -> None:
        self.updateSegment(0, 0, len(self.nums)-1, index, val)

    def sumRange(self, left: int, right: int) -> int:
        x = self.findSum(left, right, 0, len(self.nums)-1, 0)
        return x
    
    def buildSegment(self, vertex, left, right):
        if left == right:
            self.segment[vertex] = self.nums[left]
            return self.nums[left]
        
        mid = (left+right)//2
        left_child = self.buildSegment(2*vertex+1, left, mid)
        right_child = self.buildSegment((2*vertex)+2, mid+1, right)
        self.segment[vertex] = left_child + right_child
        return self.segment[vertex]
    
    def updateSegment(self, vertex, left, right, index, value):
        if left == right:
            diff = value-self.segment[vertex]
            self.segment[vertex] = value
            return diff
        
        mid = (left+right)//2
        if left <= index <= mid:
            diff = self.updateSegment(2*vertex+1, left, mid, index, value)
            self.segment[vertex] += diff
            return diff
        else:
            diff = self.updateSegment(2*vertex+2, mid+1, right, index, value)
            self.segment[vertex] += diff
            return diff
    
    def findSum(self, given_left, given_right, left, right, vertex):
        mid = (left+right)//2
        if left == given_left and right == given_right:
            return self.segment[vertex]
        elif left <= given_left <= mid and left <= given_right <= mid:
            return self.findSum(given_left, given_right, left, mid, 2*vertex+1)
        elif mid+1 <= given_left <= right and mid+1 <= given_right <= right:
            return self.findSum(given_left, given_right, mid+1, right, 2*vertex+2)
        else:
            left_overlap = self.findSum(given_left, mid, left, mid, 2*vertex+1)
            right_overlap = self.findSum(mid+1, given_right, mid+1, right, 2*vertex+2)
            return left_overlap + right_overlap

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)