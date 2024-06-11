class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        def check(limit):
            total = 0
            j = 1
            for i in range(len(nums)):
                while j < len(nums) and nums[j] - nums[i] <= limit:
                    j += 1
                total += (j - i - 1)
            return total >= k
        
        l = 0
        r = nums[-1] - nums[0]
        
        while l < r:
            mid = l + ((r - l) // 2)
            if check(mid):
                r = mid
            else:
                l = mid + 1
        
        return l