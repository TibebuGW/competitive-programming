class Solution:
        def numIdenticalPairs(self, nums: List[int]) -> int:
                toReturn = Counter(nums)
                num = 0
                for x in list(toReturn.values()):
                        num += x*(x-1)/2 

                return num
        
        
############## Trial 2 ###########
# class Solution:
        
#     def numIdenticalPairs(self, nums: List[int]) -> int:
#         def fact(y) -> int:
#             if(y == 1 or y == 0):
#                 return 1
#             else:
#                 return y*fact(y-1)
            
#         toReturn = Counter(nums)
#         num = 0
        
#         for x in list(toReturn.values()):
#             if x > 1:
#                 num += fact(x)/(2*fact(x-2))
#             else: 
#                 continue
              
#         return int(num)
      
      
############# Trial 1 ##########
# class Solution:
#   def numIdenticalPairs(self, nums: List[int]) -> int:
#       toReturn = 0
#       for i in range(0, len(nums)):
#            for j in range(i+1, len(nums)):
#                 if nums[i] == nums[j]:
#                     toReturn += 1
#       return toReturn
    
    
