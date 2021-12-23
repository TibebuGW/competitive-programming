class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = list(zip(position, speed))
        count = 0
        stack = []
        time = []
        
            
        arr.sort(reverse = True)
        print(arr)
        
        for i,j in arr:
            time.append((target-i)/j)
            
        print(time)
        
        
        for i in range(0, len(time)):
            if stack and time[i] > stack[-1]:
                
                while stack and stack[-1] < time[i]:
                    stack.pop()
                
                if not stack:
                    count += 1
                stack.append(time[i])
            else:
                if not stack:
                    count += 1
                stack.append(time[i])
            
        
        
        
        return(count)
                            
        
        
    
        
