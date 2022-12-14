class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # Algorithm
        # First figure out all the connected components
        # The sum of maximum number of groups in each component is the total answer
        # A connected component cannot be n-partite if it cannot be bipartite
        # If one of the components is not bipartite, return -1
        # After figuring out all the connected components, find the MAXIMUM DEPTH in each connected component
        # That is the maximum coloring we can apply to the component
        # Return the sum of all connected components' maximum depths(groups or colorings)
        parent = [i for i in range(n)]
        def find(node):
            if node == parent[node]:
                return node
            return find(parent[node])
        
        def union(node1, node2):
            parent1 = find(node1)
            parent2 = find(node2)
            
            if parent1 != parent2:
                if indegree[parent1] < indegree[parent2]:
                    parent[parent2] = parent1
                else:
                    parent[parent1] = parent2
        
        
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for src, dst in edges:
            graph[src - 1].append(dst - 1)
            graph[dst - 1].append(src - 1)
            indegree[src - 1] += 1
            indegree[dst - 1] += 1
        
        
        def isBipartite(node):
            set_a = set()
            set_b = set()
            set_a.add(node)
            queue = deque([(node, "a")])
            while queue:
                size = len(queue)
                for _ in range(size):
                    cur_node, tag = queue.popleft()
                    next_tag = "a" if tag == "b" else "b"
                    for nei in graph[cur_node]:
                        if tag == "a":
                            if nei in set_a:
                                return False
                            elif nei not in set_b:
                                set_b.add(nei)
                                queue.append((nei, next_tag))
                        else:
                            if nei in set_b:
                                return False
                            elif nei not in set_a:
                                set_a.add(nei)
                                queue.append((nei, next_tag))
            return True
        
        def bfs(node):
            level = 0
            queue = deque([node])
            visited = set({node})
            while queue:
                size = len(queue)
                for _ in range(size):
                    node = queue.popleft()
                    for nei in graph[node]:
                        if nei not in visited:
                            visited.add(nei)
                            queue.append(nei)
                level += 1
            return level
        
        for src, dst in edges:
            union(src - 1, dst - 1)
        
        
        total = 0
        d = defaultdict(int)
        for i in range(n):
            if not isBipartite(i):
                return -1
            p = find(i)
            d[p] = max(d[p], bfs(i))
        
        for key, val in d.items():
            total += val
        return total