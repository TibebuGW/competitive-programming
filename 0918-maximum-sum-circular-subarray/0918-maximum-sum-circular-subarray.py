class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        def cross_sum(l,r):
            mid = (l+r)//2
            left_cur = left_max = float('-inf')
            for i in range(mid, l-1, -1):
                if i == mid:
                    left_cur = left_max = nums[i]
                else:
                    left_cur += nums[i]
                    left_max = max(left_max, left_cur)
            right_cur = right_max = float('-inf')
            for i in range(mid+1, r+1):
                if i == mid+1:
                    right_cur = right_max = nums[i]
                else:
                    right_cur += nums[i]
                    right_max = max(right_max, right_cur)
            
            return left_max+right_max
        
        def solve(l, r):
            if l == r:
                return nums[l]
            
            mid = (l+r)//2
            left_max = solve(l, mid)
            right_max = solve(mid+1, r)
            crossing_max = cross_sum(l,r)
            return max(left_max, right_max, crossing_max)
        
        left_end = [nums[0]]
        left_max = left_cur = nums[0]
        right_end = [nums[-1]]
        right_max = right_cur = nums[-1]
        for i in range(1,len(nums)):
            left_cur += nums[i]
            left_max = max(left_max, left_cur)
            left_end.append(left_max)
        for i in range(len(nums)-2, -1, -1):
            right_cur += nums[i]
            right_max = max(right_max, right_cur)
            right_end.append(right_max)
        right_end = right_end[::-1]
        max_ = float('-inf')
        for i in range(len(nums)-1):
            max_ = max(left_end[i]+right_end[i+1], max_)
        return max(solve(0, len(nums)-1), max_)