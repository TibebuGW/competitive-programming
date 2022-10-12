class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        def cross_sum(l, r):
            mid = (l+r)//2
            left_sum_max = nums[mid]
            left_sum_cur = nums[mid]
            for i in range(mid-1, l-1,-1):
                left_sum_cur += nums[i]
                left_sum_max = max(left_sum_max, left_sum_cur)
            right_sum_max = nums[mid+1]
            right_sum_cur = nums[mid+1]
            for i in range(mid+2, r+1):
                right_sum_cur += nums[i]
                right_sum_max = max(right_sum_max, right_sum_cur)
            
            # print(left_sum_max, right_sum_max)
            
            return left_sum_max+right_sum_max
        
        def solve(l, r):
            if l == r:
                return nums[l]
            
            mid = (l+r)//2
            max_left_subarray = solve(l, mid)
            max_right_subarray = solve(mid+1, r)
            max_crossing_subarray = cross_sum(l, r)
            return max(max_left_subarray, max_right_subarray, max_crossing_subarray)
        
        return solve(0, len(nums)-1)