class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        toReturn = []
        def isArithmetic(arr: List[int])-> bool:
            print(arr)
            arr.sort()
            diff = arr[1] - arr[0]
            for j in range(2, len(arr), 1):
                if arr[j] - arr[j-1] != diff:
                    return False
                else:
                    continue
                
            return True
        
        
        for i in range(0, len(r), 1):
            if isArithmetic(nums[l[i]:r[i]+1]):
                toReturn.append(True)
            else:
                toReturn.append(False)
                
                
        return toReturn
