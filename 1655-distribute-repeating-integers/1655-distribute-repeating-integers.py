class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        
        @lru_cache(None)
        def dp(index, mask):
            if not mask:
                return True
            if index == n:
                return False
            
            submask = mask
            flag = False
            while submask:
                if total[submask] <= arr[index] and dp(index+1, submask^mask):
                    flag = True
                    break
                submask = (submask-1) & mask
            if flag:
                return True
            else:
                return dp(index+1, mask)
        
        
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        arr = list(d.values())
        
        n = len(arr)
        m = len(quantity)
        total = [0]*(1<<m)
        
        for mask in range(1<<m):
            for i in range(m):
                if (1<<i) & mask:
                    total[mask] += quantity[m-1-i]
        
        return dp(0, (1<<m)-1)