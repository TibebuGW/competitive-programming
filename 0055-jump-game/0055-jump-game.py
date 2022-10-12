class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums)-1
        for i in range(len(nums)-2, 0, -1):
            if last <= i+nums[i]:
                last = i
        return nums[0] >= last
            