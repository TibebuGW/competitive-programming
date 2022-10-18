class Solution:
    def totalSubarrays(self, n):
        return n*(n-1)//2
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        result = 0
        difference_arr = [nums[i]-nums[i-1] for i in range(1, len(nums))]

        l = 0
        while l < len(difference_arr):
            r = l+1
            while r < len(difference_arr) and difference_arr[r] == difference_arr[l]:
                r += 1
            if r-l >= 2:
                result += self.totalSubarrays(r-l)
            l = r
        
        return result
        
        