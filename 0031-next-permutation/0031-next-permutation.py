class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def reverseSort(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        if len(nums) == 1:
            return
        
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                next_bigger_index = i + 1
                for j in range(i + 1, len(nums)):
                    if nums[j] > nums[i] and nums[j] <= nums[next_bigger_index]:
                        next_bigger_index = j
                
                nums[i], nums[next_bigger_index] = nums[next_bigger_index], nums[i]
                l = i + 1
                r = len(nums) - 1
                reverseSort(l, r)
                
                return
        
        reverseSort(0, len(nums) - 1)
        return