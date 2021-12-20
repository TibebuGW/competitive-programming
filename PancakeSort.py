class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        toReturn = []
        for i in range(0, len(arr), 1):
            if arr.index(len(arr)-i) == len(arr)-i-1:
                continue
            else:
                print(arr.index(len(arr)-i))
                x = arr.index(len(arr)-i) 
                arr[0:x+1] = arr[0:x+1][::-1]
                toReturn.append(x+1)
                y = len(arr)-i-1
                arr[0:y+1] = arr[0:y+1][::-1]
                toReturn.append(y+1)
        return toReturn
