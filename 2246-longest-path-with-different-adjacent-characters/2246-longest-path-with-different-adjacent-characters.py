class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        for index, p in enumerate(parent):
            graph[p].append(index)
        
        max_ = [0]
        def dfs(node = 0):
            
            children_maximums = [(0, "*"), (0, "*")]
            for nei in graph[node]:
                cur_max, cur_char = dfs(nei)
                cur = 1 if s[node] != s[nei] else 0
                max_[0] = max(max_[0], cur_max + cur)
                heappush(children_maximums, (-cur_max, cur_char))
            
            temp = []
            while children_maximums:
                length, char = heappop(children_maximums)
                if char != s[node]:
                    temp.append([length, char])
                    if temp == 2:
                        break
                        
            first_biggest = temp[0]
            second_biggest = temp[1]
            
            max_[0] = max(max_[0], -first_biggest[0] + -second_biggest[0] + 1)
            
            if first_biggest[1] != s[node]:
                return (-first_biggest[0] + 1, s[node])
            elif second_biggest[1] != s[node]:
                return (-second_biggest[0] + 1, s[node])
            else:
                while children_maximums:
                    next_biggest = heappop(children_maximums)
                    if next_biggest[1] != s[node]:
                        return (-next_biggest[0] + 1, s[node])
            
            return (1, s[node])
        
        dfs()
        return max_[0]