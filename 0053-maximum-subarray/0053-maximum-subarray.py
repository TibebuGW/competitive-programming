class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        
        pre, suf = [*nums], [*nums]
        for i in range(1, len(nums)):       pre[i] += max(0, pre[i-1])
        for i in range(len(nums)-2,-1,-1):  suf[i] += max(0, suf[i+1])
        # print(pre)
        # print(suf)
        def solve(l, r):
            if l == r:
                return nums[l]
            
            mid = (l+r)//2
            max_left_subarray = solve(l, mid)
            max_right_subarray = solve(mid+1, r)
            # max_crossing_subarray = cross_sum(l, r)
            return max(max_left_subarray, max_right_subarray, pre[mid]+suf[mid+1])
        
        return solve(0, len(nums)-1)