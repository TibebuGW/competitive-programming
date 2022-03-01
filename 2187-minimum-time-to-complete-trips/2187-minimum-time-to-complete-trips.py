class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def helper(t):
            count = 0
            for i in range(len(time)):
                count += math.floor(t/time[i])
                
            print("count:", count)
            return count
        
        
        left = min(time)
        right = min(time)*totalTrips
        print(left, right)
        best = right
        
        while left <= right:
            mid = (left+right)//2
            print(mid)
            temp = helper(mid)
            if temp < totalTrips:
                # best = min(best, mid)
                left = mid+1
            else:
                right = mid-1
            # else:
            #     return mid
                
                
        return left