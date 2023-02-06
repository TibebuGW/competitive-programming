class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.x_axis = defaultdict(set)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1
        if point[0] in self.x_axis:
            self.x_axis[point[0]].add(tuple(point))
        else:
            self.x_axis[point[0]] = set({tuple(point)})
            

    def count(self, point: List[int]) -> int:
        total = 0
        for first_point in self.x_axis[point[0]]:
            if point[1] > first_point[1]:
                diff = point[1] - first_point[1]
                second_point1 = (point[0] - diff, point[1] - diff)
                third_point1 = (point[0] - diff, point[1])
                total += self.points[first_point] * self.points[second_point1] * self.points[third_point1]
                
                second_point2 = (point[0] + diff, point[1] - diff)
                third_point2 = (point[0] + diff, point[1])
                total += self.points[first_point] * self.points[second_point2] * self.points[third_point2]

            elif point[1] < first_point[1]:
                diff = first_point[1] - point[1]
                second_point1 = (point[0] - diff, point[1] + diff)
                third_point1 = (point[0] - diff, point[1])
                total += self.points[first_point] * self.points[second_point1] * self.points[third_point1]                
                second_point2 = (point[0] + diff, point[1] + diff)
                third_point2 = (point[0] + diff, point[1])
                total += self.points[first_point] * self.points[second_point2] * self.points[third_point2]
        
        return total
# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)