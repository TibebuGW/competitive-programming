class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]
        
        for i in range(1, len(nums)):
            if nums[i] > sub[-1]:
                sub.append(nums[i])
            elif nums[i] == sub[-1]:
                continue
            else:
                best = -1
                l = 0
                r = len(sub)-1
                while l <= r:
                    mid = (l+r)//2
                    if sub[mid] > nums[i]:
                        best = mid
                        r = mid -1
                    elif sub[mid] == nums[i]:
                        best = mid
                        break
                    else:
                        l = mid + 1
                
                sub[best] = nums[i]
            # print(sub)
        
        return len(sub)