class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        n = len(arr)
        toReturn = 0
        
        values = list(count.values())
        values.sort(reverse=True)
        
        print(values)
        if values[0] >= n/2:
            toReturn = 1
            return toReturn
        
        total = values[0]
        for i in range(1, len(values), 1):
            j = 0
            
            if values[i] + total  >= n/2:
                toReturn = i + 1
                return toReturn
            else:
                total += values[i]
                continue

        return toReturn
