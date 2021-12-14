class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        counter = collections.Counter(changed)
        toReturn = []
        # if counter[0]%2 or len(changed)%2:
        #     return []
        
        for x in sorted(changed):
            if counter[x] > 0:
                counter[x] -= 1
                if counter[x*2] > 0:
                    counter[x*2] -= 1
                    toReturn.append(x)
                else:
                    return []
                
        return toReturn
            
        print(counter)
