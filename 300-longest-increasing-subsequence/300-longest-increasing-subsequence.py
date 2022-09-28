class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        path = [nums[0]]        
        for i in range(1, len(nums)):
            if nums[i] > path[-1]:
                path.append(nums[i])
            else:
                l = 0
                r = len(path)-1
                best = 0
                while l <= r:
                    mid = (l+r)//2
                    if path[mid] > nums[i]:
                        best = mid
                        r = mid-1
                    elif path[mid] < nums[i]:
                        l = mid+1
                    else:
                        best = mid
                        break
                path[best] = nums[i]
        
        return len(path)