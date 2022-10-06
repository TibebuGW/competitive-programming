class TimeMap:

    def __init__(self):
        self.main = defaultdict(dict)
        self.max = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.main[key][timestamp] = value
        self.max[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        # print("here 1")
        l = 0
        r = len(self.max[key])-1
        best = -1
        while l <= r:
            mid = (l+r)//2
            if self.max[key][mid] == timestamp:
                best = mid
                break
            elif self.max[key][mid] < timestamp:
                best = mid
                l = mid+1
            else:
                r = mid-1
        
        # print("here 2")
        if best == -1:
            return ""
        else:
            
            return self.main[key][self.max[key][best]]
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)