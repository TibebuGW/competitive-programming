class Solution:
    def intersect(self, line1, line2):
        l1Xstart, l1Ystart = line1[0]
        l1Xend, l1Yend = line1[1]
        l2Xstart, l2Ystart = line2[0]
        l2Xend, l2Yend = line2[1]
        
        if (l1Xstart <= l2Xstart <= l1Xend and l2Ystart <= l1Ystart <= l2Yend) or (l2Xstart <= l1Xstart <= l2Xend and l1Ystart <= l2Ystart <= l1Yend):
            return True
        
        return False
    
    def solve(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int):
        if (ax1 <= bx1 and ay1 <= by1 and ax2 >= bx2 and ay2 >= by2):
            return abs(ax2-ax1)*abs(ay2-ay1)
        if (ax1 >= bx1 and ay1 >= by1 and ax2 <= bx2 and ay2 <= by2):
            return abs(bx2-bx1)*(by2-by1)
        
        areaA = abs(ax2-ax1)*abs(ay2-ay1)
        areaB = abs(bx2-bx1)*abs(by2-by1)
        intersectionArea = 0
        if self.intersect([[ax1, ay2], [ax2, ay2]], [[bx1, by1], [bx1, by2]]):
            if self.intersect([[ax1, ay1], [ax2, ay1]], [[bx1, by1], [bx1, by2]]):
                intersectionPoint = [bx1, ay1]
                intersectionArea = abs(min(ax2, bx2)-bx1)*abs(ay2-ay1)
            else:
                intersectionArea = abs(min(ax2, bx2)-bx1)*abs(ay2-by1)
        elif self.intersect([[ax1, ay2], [ax2, ay2]], [[bx2, by1], [bx2, by2]]):
            if self.intersect([[ax1, ay1], [ax2, ay1]], [[bx2, by1], [bx2, by2]]):
                intersectionPoint = [bx2, ay1]
                intersectionArea = abs(bx2-max(ax1,bx1))*abs(ay2-ay1)
            else:
                intersectionArea = abs(bx2-max(ax1,bx1))*abs(ay2-by1)
        elif self.intersect([[ax1, ay1], [ax2, ay1]], [[bx1, by1], [bx1, by2]]):
            intersectionArea = abs(min(ax2, bx2)-bx1)*abs(by2-ay1)
        elif self.intersect([[ax1, ay1], [ax2, ay1]], [[bx2, by1], [bx2, by2]]):
            intersectionArea = abs(bx2-max(ax1,bx1))*abs(by2-ay1)
        elif self.intersect([[ax1, ay1], [ax1, ay2]], [[bx1, by2], [bx2, by2]]) and self.intersect([[ax2, ay1], [ax2, ay2]], [[bx1, by2], [bx2, by2]]):
            intersectionArea = abs(ax2-ax1)*abs(by2-max(ay1, by1))
        elif self.intersect([[ax1, ay1], [ax1, ay2]], [[bx1, by1], [bx2, by1]]) and self.intersect([[ax2, ay1], [ax2, ay2]], [[bx1, by1], [bx2, by1]]):
            intersectionArea = abs(ax2-ax1)*abs(min(ay2, by2)-by1)
            
            
            
        return areaA+areaB-intersectionArea
        
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        A = self.solve(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
        B = self.solve(bx1, by1, bx2, by2, ax1, ay1, ax2, ay2)
        
        return min(A, B)
        