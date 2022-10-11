class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(l, r):
            max_ = nums[l]
            prev = max_
            for i in range(l+1, r+1):
                if i == l+1:
                    max_ = max(max_, nums[i])
                else:
                    temp = max_
                    max_ = max(max_, nums[i]+prev)
                    prev = temp
            return max_
        if len(nums) < 3:
            return max(nums)
        return max(solve(0,len(nums)-2), solve(1, len(nums)-1))