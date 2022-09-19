class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        graph = defaultdict(list)
        d = defaultdict(list)
        for path in paths:
            arr = path.split(" ")
            for i in range(1, len(arr)):
                graph[arr[0]].append(arr[i])
                temp = arr[i].split("(")
                d[temp[-1][:-1]].append(arr[0]+"/"+temp[0])
        
        # print(graph)
        ans = []
        
        # print(d)
        for key, value in d.items():
            if len(value) > 1:
                ans.append(value)
        
        return ans