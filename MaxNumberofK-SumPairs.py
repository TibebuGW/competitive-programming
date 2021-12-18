class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        toReturn = 0
        count = Counter(nums)
        key = []
        key = list(count.keys())
        print(key)
        for i in range(0, len(key), 1):
            if count[key[i]] > 0 and count[k-key[i]] > 0:
                if key[i] == k-key[i]:
                    toReturn += count[key[i]]//2
                else:
                    toReturn += min(count[key[i]], count[k-key[i]])
                    count[key[i]] = count[k-key[i]] = 0
        
        
        return toReturn
