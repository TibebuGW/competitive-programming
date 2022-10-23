class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        total = 0
        for i, num in enumerate(nums):
            if nums[abs(num)-1] < 0:
                ans.append(abs(num))
            else:
                nums[abs(num)-1] *= -1
            total += abs(num)    
        n = len(nums)
        real_total = (n*(n+1))//2
        ans.append(real_total-(total-ans[0]))
        return ans