class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2 == 1:
            return []
        
        d = defaultdict(int)
        
        for num in changed:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        arr = []
        for num in sorted(changed, reverse=True):
            if num == num//2:
                if d[num]%2 == 0:
                    for i in range(d[num]//2):
                        arr.append(num)
                    d[num] = 0
                else:
                    return []
            else:
                if num%2 == 0 and d[num] and d[num//2]:
                    d[num] -= 1
                    d[num//2] -= 1
                    arr.append(num//2)
        
        return arr if len(arr)*2 == len(changed) else []