class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.race = self.helper(self.persons)
        
    def helper(self, persons):
        race = []
        people = len(set(persons))
        latestWinner = (0,0)
        
        arr = {i:0 for i in range(people)}
                
        for i in range(len(persons)):
            arr[persons[i]] += 1
            if arr[persons[i]] >= latestWinner[1]:
                latestWinner = (persons[i], arr[persons[i]])
                
            race.append(latestWinner[0])
        return race
    def q(self, t: int) -> int:
        best = len(self.times)-1
        left = 0
        right = len(self.times)-1
        
        while left <= right:
            mid = (left+right)//2
            
            if self.times[mid] <= t:
                best = mid
                left = mid+1
            else:
                right = mid-1
        
        return self.race[best]
                


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
