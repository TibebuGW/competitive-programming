class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        visited = set()
        ans = []
        
        for i in range(len(nums)-2):
            if nums[i] in visited:
                continue
            visited.add(nums[i])
            l = i+1
            r = len(nums)-1
            while l < r:
                sum_ = nums[i]+nums[l]+nums[r]
                if sum_ < 0:
                    l += 1
                elif sum_ > 0:
                    r -= 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while r > l and nums[r] == nums[r+1]:
                        r -= 1
        
        return ans