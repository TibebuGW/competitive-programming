from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        set_a = set()
        set_b = set()
        
        
        for i in range(len(graph)):
            if i not in set_a and i not in set_b:
                queue = deque([(i, "a")])
                set_a.add(i)
                while queue:
                    size = len(queue)
                    for _ in range(size):
                        node, tag = queue.popleft()
                        new_tag = "a" if tag == "b" else "b"
                        for nei in graph[node]:
                            if tag == "a":
                                if nei in set_a:
                                    return False
                                elif nei not in set_b:
                                    set_b.add(nei)
                                    queue.append((nei, new_tag))
                            else:
                                if nei in set_b:
                                    return False
                                elif nei not in set_a:
                                    set_a.add(nei)
                                    queue.append((nei, new_tag))
        
        return True