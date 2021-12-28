################ trial 2 ###############
from collections import deque
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        result = float('inf')
        q = deque()
        
        arr = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            arr[i+1] = arr[i] + nums[i]

        
        left = 0
        right = 0
        
        while right < len(arr):
            while q and arr[q[-1]] >= arr[right]:
                q.pop()
                
            q.append(right)
            
            while q and arr[right] - arr[q[0]] >= k:
                result = min(result, right-q.popleft())
            
            right += 1
            
        
        return -1 if result == float('inf') else result

################ trial 1 ###############
# from collections import deque
# class Solution:
#     def shortestSubarray(self, nums: List[int], k: int) -> int:
#         minSoFar = len(nums)
#         total = 0
#         q = deque()
        
#         # if sum(nums) < k:
#         #     print(sum(nums))
#         #     return -1
        
#         for i in range(0, len(nums)):
#             q.append(nums[i])
#             print("****")
#             print(q)
#             print("****")
#             total += nums[i]
#             if total >= k:
#                 while q and total >= k:
#                     print(q)
#                     minSoFar = min(minSoFar, len(q))
#                     total -= q.popleft()
                    
#         if len(q) == len(nums):
#             return -1
#         else:
#             # print(minSoFar)
#             return minSoFar
