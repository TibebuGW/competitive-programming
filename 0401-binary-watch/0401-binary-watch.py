class Solution:
    def bitCounter(self, num):
        count = 0
        while num:
            count += num&1
            num >>= 1
        return count
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        for hour in range(12):
            for minute in range(60):
                if self.bitCounter(hour)+self.bitCounter(minute) == turnedOn:
                    if minute<10:
                        minute = f'0{minute}'
                    ans.append(f'{hour}:{minute}')
                    
                    
        return ans