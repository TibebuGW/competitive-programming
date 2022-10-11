class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        last = -1
        stack = []
        for i, num in enumerate(nums):
            if last != -1 and num > last:
                return True
            else:
                arr = []
                while stack and num <= stack[-1]:
                    arr.append(stack.pop())
                
                if len(arr) == 2:
                    last = arr[0] if last == -1 else min(last, arr[0])
                
                stack.append(num)
                
                if len(stack) == 3:
                    return True
        
        return False
                    