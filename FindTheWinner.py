class Solution:
    def findTheWinner(self, n: int, k: int) -> int:        
        arr = list(range(1,n+1))
            
        length = len(arr)
        i = 0
        while length > 1:
            i += k-1
            i = i%length
            print (arr)
            arr.pop(i)
            length -= 1
        print(arr)
        return arr[0]
    
