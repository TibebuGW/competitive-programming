from sortedcontainers import SortedList
class TweetCounts:

    def __init__(self):
        self.main = defaultdict(SortedList)
        self.second = {'minute': 59, 'hour': 3599, 'day': 86399}

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.main[tweetName].add(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        arr = self.main[tweetName]
        chunks = []
        time = startTime
        while time <= endTime:
            chunks.append((time, min(endTime, time + self.second[freq])))
            time += self.second[freq] + 1
            
        # print(chunks)
        ans = []
        for start, end in chunks:
            left = self.upperBinarySearch(arr, start)
            right = self.lowerBinarySearch(arr, end)
            if left != len(arr) and right != -1:
                ans.append(right - left + 1)
            else:
                ans.append(0)
        
        return ans
    
    def upperBinarySearch(self, arr, start):
        l = 0
        r = len(arr) - 1
        
        best = len(arr)
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == start:
                return mid
            elif arr[mid] < start:
                l = mid + 1
            else:
                best = mid
                r = mid - 1
        
        return best
    
    def lowerBinarySearch(self, arr, end):
        l = 0
        r = len(arr) - 1
        
        best = -1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == end:
                return mid
            elif arr[mid] > end:
                r = mid - 1
            else:
                best = mid
                l = mid + 1
        
        return best

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)