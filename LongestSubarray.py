########### trial 3 ###########

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        result = 0
        
        left = 0
        right = 0
        
        minDeque = Deque()
        maxDeque = Deque()
        
        while (right < len(nums)):
            while len(minDeque) and nums[right] <= nums[minDeque[-1]]:
                minDeque.pop()
            minDeque.append(right)
                
            while len(maxDeque) and nums[right] >= nums[maxDeque[-1]]:
                maxDeque.pop()
            maxDeque.append(right)
            
            if abs(nums[maxDeque[0]] - nums[minDeque[0]]) > limit:
                left += 1
                if left > maxDeque[0]:
                    maxDeque.popleft()
                if left > minDeque[0]: 
                    minDeque.popleft()
            else:
                result = max(result, right-left+1)
                right += 1
            
        return result

############# trial 2 #################

# class Solution:
#     def longestSubarray(self, nums: List[int], limit: int) -> int:
#         result = 0
#         arrMin = max(nums)
#         if len(nums) == 1:
#             return 1
#         for i in range(0, len(nums)):
#             arrMax = nums[i]
#             arrMin = nums[i]
#             if len(nums[i:len(nums)])+1 < result:
#                 break
#             for j in range(i+1, len(nums)):
#                 # print("*****")
#                 # print(nums[i:j+1])
#                 # print(absDiff(nums[i:j]))
                
#                 if nums[j] >= arrMax:
#                     arrMax = nums[j]
                    
#                 if nums[j] <= arrMin:
#                     arrMin = nums[j]
                
#                 if abs(arrMax-arrMin) > limit:
#                     # print(j-i+1)
#                     break
#                 else:
#                     # print("works: ", j-i+1)
#                     result = max(result, j-i+1)

#         return result

############# trial 1 #################

# class Solution:
#     def longestSubarray(self, nums: List[int], limit: int) -> int:
#         stack = [0]
#         def absDiff(arr: List[int])-> int:
#             return max(arr) - min(arr)
#         for i in range(0, len(nums)):
#             if len(nums)-i > stack[-1]:
#                 for j in range(len(nums), i, -1):
#                     # print("*****")
#                     # print(nums[i:j])
#                     # print(absDiff(nums[i:j]))
                   
#                     if absDiff(nums[i:j]) <= limit:
#                         length = j-i
#                         if stack and length <= stack[-1]:
#                             # print(stack)
#                             break
#                         else:
#                             while stack and stack[-1] < length:
#                                 stack.pop()
#                             stack.append(j-i)
#                             # print(stack)
#             else:
#                 break
#         #print(stack)
#         return stack[0]
        

