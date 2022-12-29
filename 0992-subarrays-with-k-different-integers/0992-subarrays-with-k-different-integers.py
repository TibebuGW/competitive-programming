class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        ans = 0
        l = 0
        d = {}
        
        for r in range(len(nums)):
            if nums[r] in d:
                d[nums[r]] += 1
            else:
                d[nums[r]] = 1
            
            while len(d) > k:
                d[nums[l]] -= 1
                if d[nums[l]] == 0:
                    del d[nums[l]]
                l += 1
            
            if len(d) == k:
                first_distinct_index = l
                while d[nums[first_distinct_index]] > 1:

                    if d[nums[first_distinct_index]] != 0:
                        d[nums[first_distinct_index]] -= 1

                    first_distinct_index += 1

                temp = first_distinct_index - 1

                while temp >= l:
                    if nums[temp] in d:
                        d[nums[temp]] += 1
                    else:
                        d[nums[temp]] = 1

                    temp -= 1

                ans += (first_distinct_index - l + 1) * int(len(d) == k)
        
        return ans