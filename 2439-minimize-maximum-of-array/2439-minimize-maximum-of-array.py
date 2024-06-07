class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        def checkValue(value):
            to_be_added = 0
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] > value:
                    to_be_added += (nums[i] - value)
                else:
                    to_be_added = max(0, to_be_added - (value - nums[i]))
            
            return not to_be_added
        
        l = 0
        r = max(nums)
        best_ans = r
        while l <= r:
            mid = (l + r) // 2
            if checkValue(mid):
                best_ans = min(best_ans, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return best_ans