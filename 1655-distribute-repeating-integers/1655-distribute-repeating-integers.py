class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        # the idea of the question is that we want to fit all customers' requirements into appropriate number of integers. the key word here is appropriate. take the question as, we want to fit items(quantities) of some sizes in boxes(nums) of some sizes. trying to fit an item into the next box which has equal or greater size (greedy) might not be the optimal way. because for example if nums = [10,10,10,10,20,20,20] (this can be reduced to a box of size 4 and a box of size 3) and quantity = [3,2,2] if we try to fit 3 into the box which has size 4 and fit 2 into size 3, that yields false answer as the last 2 will not have anywhere to fit in ([1,1]). so it's not about whether the item can fit or not but rather how well an item fits into a box or another way of saying it is how can we use a box to fit as many items as possible. therefore doing all possible combinations is the only way. for that we use dp. while using dp, since the size of quantity is at most 10 we can store the information about the quantities in a number whose bit length == len(quantity). that means for every quantity we have 1 bit reserved for it. 1 denotes the quantity is yet to find a box while 0 means that quantity has been fitted somewhere. so at the start all bits are 1 and we do a combination of those bits which are 1 and try to fit them into a box. one optimization is that before we start to check every combination for a box, we can store the sum of quantities of all possible combinations of quantities in an array and just do a lookup when we need to check if some combination of quantities is appropriate for a box.
        
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