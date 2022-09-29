class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        d = defaultdict(list)
        total = 1
        total_without_zero = 1
        for i in range(len(nums)):
            d[nums[i]].append(i)
            total *= nums[i]
            if nums[i]:
                total_without_zero *= nums[i]
        
        if len(d[0]) > 1:
            return [0]*len(nums)
        elif len(d[0]) == 1:
            return [0]*d[0][0] + [total_without_zero] + [0]*(len(nums)-d[0][0]-1)
        else:
            for i in range(len(nums)):
                nums[i] = total//nums[i]
            return nums