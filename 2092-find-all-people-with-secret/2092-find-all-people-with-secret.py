class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        parent = [i for i in range(n)]
        parent[firstPerson] = 0
       
        rank = [1 for i in range(n)]
        rank[0] = 2
        times = defaultdict(list)
        
        def find(a):
            if a == parent[a]:
                return a
            return find(parent[a])
        
        def union(a, b):
            a = find(a)
            b = find(b)
            
            if a != b:
                if rank[a] > rank[b]:
                    parent[b] = a
                    rank[a] += rank[b]
                else:
                    parent[a] = b
                    rank[b] += rank[a]
                    
        union(firstPerson, 0)
        
        for x, y, time in meetings:
            times[time].append((x, y))
            
            
        time_array = list(times.keys())
        time_array.sort()
        
        for index in time_array:
            pool = set()
            for x, y in times[index]:
                union(x, y)
                pool.add(x)
                pool.add(y)
                
            zero = find(0)
            for num in pool:
                if find(num) != zero:
                    parent[num] = num
            
        zero = find(0)
        result = [i for i in range(len(parent)) if find(i) == zero]
        return result