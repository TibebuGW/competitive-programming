class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for path in paths:
            arr = path.split(" ")
            for i in range(1, len(arr)):
                temp = arr[i].split("(")
                d[temp[-1][:-1]].append(arr[0]+"/"+temp[0])
        
        ans = []
        for key, value in d.items():
            if len(value) > 1:
                ans.append(value)
        
        return ans