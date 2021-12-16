class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0 
        right = 0 
        maxFreq = 0 
        total = 0
        
        while right < len(nums):
            total += nums[right]
            if nums[right]*(right-left+1) <= total+k:
                maxFreq += 1
            else: 
                total -= nums[left]
                left += 1
                
            right += 1
            
    
        return maxFreq
    
############  First Trial ############## 
# class Solution:
#     def maxFrequency(self, nums: List[int], k: int) -> int:
#         nums.sort(reverse=True)
#         toReturn = {}
#         temp = k
        
        
#         for i in range(0, len(nums), 1):
#             #nums = arr
#             toReturn[nums[i]] = 1
#             #print(toReturn)
#             k = temp
            
#             for j in range(i+1, len(nums), 1):
#                 if nums[i] == nums[j]:
#                     toReturn[nums[i]] += 1
#                     continue
#                 if nums[i] - nums[j] <= k:
#                     #nums[j] += (nums[i] - nums[j])
#                     k -= (nums[i] - nums[j])
#                     toReturn[nums[i]] += 1
#                     #print(nums)
#                 else:

#                     break

#             #toReturn[nums[i]] = nums.count(nums[i])
                
#         print(toReturn)
#         return max(toReturn.values())
