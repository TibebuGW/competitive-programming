################ trial 2 ###############


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
