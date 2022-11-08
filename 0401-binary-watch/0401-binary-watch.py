class Solution:
    def __init__(self):
        self.minute_array = []
        self.hour_array = []
        
    def hour_combination(self, arr, k, total, index):
        if k >= 4:
            return
        
        if k == 0:
            if total<12:
                self.hour_array.append(str(total))
            return
        
        for i in range(index, len(arr)):
            total += arr[i]
            self.hour_combination(arr, k-1, total, i+1)
            total -= arr[i]
            
    def minute_combination(self, arr, k, total, index):
        if k >= 6:
            return
        
        if k == 0:
            if 10<=total<=59:
                self.minute_array.append(str(total))
            elif 0<=total<10:
                self.minute_array.append("0"+str(total))
            return
                
        for i in range(index, len(arr)):
            total += arr[i]
            self.minute_combination(arr, k-1, total, i+1)
            total -= arr[i]
            
    def readBinaryWatch(self, turnedOn: int) -> List[str]:        
        ans = []
        minute_k = turnedOn
        hour_k = 0
        for i in range(turnedOn+1):
            self.minute_combination([1, 2, 4, 8, 16, 32], minute_k, 0, 0)
            self.hour_combination([1, 2, 4, 8], hour_k, 0, 0)
            
            for hour in self.hour_array:
                for minute in self.minute_array:
                    ans.append(hour+":"+minute)
            self.minute_array = []
            self.hour_array = []
            minute_k -= 1
            hour_k += 1
        ans.sort()
        return ans