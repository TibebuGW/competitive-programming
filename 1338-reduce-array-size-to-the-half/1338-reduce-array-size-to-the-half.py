class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        half = len(arr)//2
        d = {}
        for num in arr:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
                
        # print(d)
        d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        # print(d)
        count = 0
        for key, value in d.items():
            if half-value>0:
                half -= value
                count += 1
            else:
                break
        
        count += 1
        return count
        