class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # arr = [nums[i] +nums[i+1] for i in range(len(nums)-1)]
        # print(arr)
        arr = [0]
        for i in range(len(nums)):
            arr.append(nums[i]+arr[-1])
            
        print(arr)
        index = -1
        for i in range(1, len(arr)):
            if arr[i-1] == arr[-1]-arr[i]:
                return i-1
        return -1