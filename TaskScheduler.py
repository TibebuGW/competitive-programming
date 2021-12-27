
######## trial 2 ###########

import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        result = 0
        resArr = []
        q = deque()
        
        count = Counter(tasks)
        a = dict(count)
        b = [[-1*v,k] for k, v in list(a.items())]
        
        heapq.heapify(b)
        print(b)
        
        while b:
            i = 0
            while i < n+1:
                if b:
                    c = heapq.heappop(b)
                    resArr.append(c[1])
                    q.append(c)
                    result += 1
                    i += 1
                else:
                    result += 1
                    resArr.append("idle")
                    i += 1
            while len(q) != 0:
                x = q.popleft()
                x[0] += 1
                if x[0] < 0:
                    b.append(x)
                    
            heapq.heapify(b)
        
        while resArr[-1] == "idle":
            resArr.pop()
            
        print(resArr)
        return len(resArr)




########### trial 1 ###########
# import heapq
# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) -> int:
#         result = 0
#         resArr = []
        
#         count = Counter(tasks)
#         a = dict(count)
#         # print((a.items()))
        
#         b = [[-1*v,k] for k, v in sorted(a.items(), key = lambda x: x[1], reverse=True)]
#         # print(b)
        
#         heapq.heapify(b)
#         print(b)
        
#         c = heapq.heappop(b)
#         print(c)
#         print(b)
        
       
#         while c[0] < 0:
#             print("^^^^^^")
#             print("current biggest element:", c[1])
#             print("^^^^^^")
#             resArr.append(c[1])
#             result += 1
#             i = 0
#             while b and i < n:
#                 # print("LARGEST: ", heapq.nlargest(1,b)[0][0])

#                 x = heapq.heappop(b)
#                 print("**********")
#                 print("popped: ", x)
#                 print(b)
#                 x[0] += 1
#                 resArr.append(x[1])
#                 print("resulting array: ", resArr)
#                 result += 1
#                 if x[0] != 0:
#                     b.append(x)
#                 print(b)
#                 i += 1
            
#             c[0] += 1
#             b.append(c)
#             heapq.heapify(b)
#             print("heapified: ", b)
#             if heapq.nlargest(1, b)[0][1] == c[1]:
#                 result += 1*n
#                 #resArr.append("idle {}".format())
#                 continue
#             c = heapq.heappop(b)
            
        
#         print(resArr)
#         return result
            
        
        
        
        
        
