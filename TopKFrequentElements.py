class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        options = Counter(nums)
        toReturn = []
       
        arr = sorted(options, key=options.get, reverse=True)
        for i in range(0, k, 1):
            toReturn.append(arr[i])
        
        return toReturn
