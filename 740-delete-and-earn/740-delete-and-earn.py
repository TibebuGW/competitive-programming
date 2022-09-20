class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        d = {}
        min_ = float('inf')
        max_ = 0
        for num in nums:
            if num < min_:
                min_ = num
            if num > max_:
                max_ = num
                
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        arr = []
        for i in range(min_, max_+1):
            if i in d:
                arr.append(i*d[i])
            else:
                arr.append(0)
        
        if len(arr) == 1:
            return arr[0]
        arr[1] = max(arr[0], arr[1])
        
        for i in range(2, len(arr)):
            arr[i] = max(arr[i]+arr[i-2], arr[i-1])
        
        return arr[-1]