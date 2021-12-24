class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        stack = [0]
        def absDiff(arr: List[int])-> int:
            return max(arr) - min(arr)
        #nums.sort()
            
        
        for i in range(0, len(nums)):
            if len(nums)-i > stack[-1]:
                for j in range(len(nums), i, -1):
                    # print("*****")
                    # print(nums[i:j])
                    # print(absDiff(nums[i:j]))
                    
                    # if j-i < stack[-1]:
                    #     break
                   
                    if absDiff(nums[i:j]) <= limit:
                        length = j-i
                        if stack and length <= stack[-1]:
                            # print(stack)
                            # stack.append(length)
                            break
                        else:
                            while stack and stack[-1] < length:
                                stack.pop()
                            stack.append(j-i)
                            # print(stack)
            else:
                break
        #print(stack)
        return stack[0]
        
#         while nums and nums[-1] - nums[0] >= limit:
#             nums.pop()
#             print(nums)
            
#         return(len(nums))
