class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        visited = set()
        def threeSum(index, target) -> List[List[int]]:
            visited = set()
            ans = []

            for i in range(index, len(nums)-2):
                if nums[i] in visited:
                    continue
                visited.add(nums[i])
                l = i+1
                r = len(nums)-1
                while l < r:
                    sum_ = nums[i]+nums[l]+nums[r]
                    if sum_ < target:
                        l += 1
                    elif sum_ > target:
                        r -= 1
                    else:
                        ans.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < len(nums) and nums[l] == nums[l-1]:
                            l += 1
                        while r > 0 and nums[r] == nums[r+1]:
                            r -= 1

            return ans
        for i in range(len(nums)-3):
            if nums[i] in visited:
                continue
            visited.add(nums[i])
            arr = threeSum(i+1, target-nums[i])
            for a in arr:
                result.append([nums[i]] + a)
        return result
        