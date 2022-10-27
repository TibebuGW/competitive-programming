class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = [0]
        for num in nums:
            prefix.append(num+prefix[-1])
        
        d = {0:0}
        if prefix[1]%k not in d:
            d[prefix[1]%k] = 1
        for i in range(2,len(prefix)):
            if prefix[i]%k not in d:
                d[prefix[i]%k] = i
            else:
                if d[prefix[i]%k] < i-1:
                    return True
        # print(d)
        return False