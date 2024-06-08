class TweetCounts:

    def __init__(self):
        self.d = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.d[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        chunks = self.getChunks(startTime, endTime, freq)
        ans = [0 for _ in range(len(chunks))]
        for time in self.d[tweetName]:
            if startTime <= time <= endTime:
                index = self.getIndex(chunks, time)
                ans[index] += 1
        
        return ans
    
    def getChunks(self, start, end, chunkType):
        ans = []
        startingTime = start
        adder = 59
        if chunkType == "hour":
            adder = 3599
        elif chunkType == "day":
            adder = 86399
        
        while startingTime <= end:
            ans.append([startingTime, min(end, startingTime + adder)])
            startingTime += adder + 1
        
        
        return ans
    
    def getIndex(self, chunks, time):
        l = 0
        r = len(chunks) - 1
        while l <= r:
            mid = (l + r) // 2
            if chunks[mid][0] <= time <= chunks[mid][1]:
                return mid
            elif time < chunks[mid][0]:
                r = mid - 1
            else:
                l = mid + 1
        
# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)