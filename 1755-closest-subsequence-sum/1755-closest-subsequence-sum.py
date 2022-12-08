class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        # print(len(nums))
        set_A = set()
        set_B = set()
        n = len(nums)
        ans = float('inf')
        def dfs(i,cur,arr,sums):
            if i==len(arr):
                sums.add(cur)
                return
            dfs(i+1,cur,arr,sums)
            dfs(i+1,cur+arr[i],arr,sums)
        
        
        dfs(0,0,nums[:len(nums)//2],set_A)
        dfs(0,0,nums[len(nums)//2:],set_B)
        
        set_A.add(0)
        set_B.add(0)
        
        arr_A = list(set_A)
        arr_B = list(set_B)
        arr_A.sort()
        # print(arr_A)
        # print(arr_B)
        
        for num in arr_B:
            num_to_search = goal - num
            
            l = 0 
            r = len(arr_A)-1
            best = -1
            while l <= r:
                mid = (l + r)//2
                if arr_A[mid] < num_to_search:
                    l = mid + 1
                    best = mid
                elif arr_A[mid] > num_to_search:
                    r = mid - 1
                else:
                    best = mid
                    break
                    
            
            minimum = 0
            if best == -1:
                minimum = arr_A[0]
            elif 0 <= best < len(arr_A) - 1:
                if best == -1:
                    best = 0
                print(best)
                if num_to_search - arr_A[best] <= arr_A[best + 1] - num_to_search:
                    minimum = arr_A[best]
                else:
                    minimum = arr_A[best + 1]
            else:
                minimum = arr_A[-1]
                
            ans = min(ans, abs(minimum+num - goal))
            if ans == 0:
                return 0
        
        return ans