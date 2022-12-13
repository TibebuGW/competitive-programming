class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan_distance(p1, p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        path = [] # path of the minimum spanning tree starting from 0
        total_cost = 0 # cost of the minimum spanning tree
        visited = set()
        
        queue = [(0, (points[0][0], points[0][1]), (-10**7, -10**7))] # "cost" to reach "node" with "parent"
        
        while queue:
            
            cost, node, parent = heappop(queue)
            if node not in visited:
                visited.add(node)
                path.append((node, parent))
                total_cost += cost
                for p in points:
                    point = (p[0], p[1])
                    if point != node and point not in visited:
                        cur_cost = manhattan_distance(point, node)
                        heappush(queue, (cur_cost, (point[0], point[1]), node))
        
        return total_cost