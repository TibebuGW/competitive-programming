class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        size = defaultdict(int)
        ans = []
        parent = [i for i in range(len(accounts))]
        d = {}
        added = {}
        
        for i in range(len(accounts)):
            size[i] = len(accounts[i])-1
        
        def find(a):
            while a != parent[a]:
                a = parent[a]
            return a
        
        def union(a, b):
            a = find(a)
            b = find(b)
            
            if a != b:
                if size[a] > size[b]:
                    parent[b] = a
                    size[a] += size[b]
                else:
                    parent[a] = b
                    size[b] += size[a]
                    
        def merge(i, j, flag):
            if flag == 0:
                temp = [accounts[i][0]] 
                temp2 = accounts[i][1:] + accounts[j][1:]
                temp2 = list(set(temp2))
                temp2.sort()
                return temp+temp2
            else:
                temp = [accounts[i][0]] 
                temp2 = accounts[i][1:] + ans[j][1:]
                temp2 = list(set(temp2))
                temp2.sort()
                return temp+temp2
            
        
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                if accounts[i][j] in d.keys():
                    # print(d)
                    union(i, d[accounts[i][j]])
                    # print(parent)
                else:
                    d[accounts[i][j]] = i
        
        # print(d)
        # print(parent)
                    
        for i in range(len(parent)):
            if i != parent[i]:
                root_parent = find(parent[i])
                if root_parent in added.keys():
                    ans[added[root_parent]] = merge(i, added[root_parent], 1)
                    added[i] = added[root_parent]
                else:
                    idx = len(ans)
                    added[i] = idx
                    added[root_parent] = idx
                    ans.append(merge(i, root_parent,0))
            else:
                if parent[i] not in added.keys():
                    idx = len(ans)
                    added[i] = idx
                    temp = [accounts[i][0]] 
                    temp2 = accounts[i][1:]
                    temp2 = list(set(temp2))
                    temp2.sort()
                    ans.append(temp + temp2)
                
            
#         for i in range(len(parent)):
#             if i not in added:
                
                
        return ans
        
        