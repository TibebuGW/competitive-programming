class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if num in d:
                d[num] += num
            else:
                d[num] = num
        
        arr =[[x,y] for x, y in sorted(d.items(), key=lambda x: x[0])]
        for i in range(1, len(arr)):
            if arr[i][0] == arr[i-1][0]+1:
                if i == 1:
                    arr[i][1] = max(arr[i][1], arr[i-1][1])
                else:
                    arr[i][1] = max(arr[i][1]+arr[i-2][1], arr[i-1][1])
            else:
                arr[i][1] += arr[i-1][1]
        
        return arr[-1][1]