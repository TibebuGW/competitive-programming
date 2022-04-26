# https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def find_set(i):
            if i == parent[i]:
                return i
            parent[i] = find_set(parent[i])
            return parent[i]
        
        def union_sets(i, j):
            a = find_set(i)
            b = find_set(j)
            if a!=b:
                if size[a] >= size[b]:
                    parent[b] = a
                    size[a] += size[b]
                else:
                    parent[a] = b
                    size[b] += size[a]
                    
        graph, parent, size, owner = [], defaultdict(int), defaultdict(int), {}
        for idx, account in enumerate(accounts):
            for i in range(1,len(account)):
                parent[account[i]] = account[i]
                size[account[i]] = 1
                owner[account[i]] = idx
                for j in range(i+1, len(account)):
                    graph.append((account[i], account[j]))
                    
        for con in graph:
            union_sets(con[0], con[1])
            
        
        answer = defaultdict(list)
        for k, v in parent.items():
            answer[owner[find_set(v)]].append(k)
        res = []
        for x, y in answer.items():
            a = [accounts[x][0]]
            a.extend(sorted(y))
            res.append(a)
            
        return res
                
                
                