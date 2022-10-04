class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        left = [-1]*len(strength)
        right = [len(strength)]*len(strength)
        
        stack = []
        
        for i in range(len(strength)):
            while stack and strength[i] < strength[stack[-1]]:
                right[stack.pop()] = i
            stack.append(i)
        
        
        stack = []
        
        for i in range(len(strength)-1, -1, -1):
            while stack and strength[i] <= strength[stack[-1]]:
                left[stack.pop()] = i
            stack.append(i)
        
        ac = list(accumulate(strength))
        acc = list(accumulate(ac, initial=0))
        
#         print(left)
#         print(right)
        total = 0
        
        for i in range(len(strength)):
            l, r = left[i], right[i]
            lacc = acc[i]-acc[max(l, 0)]
            racc = acc[r]-acc[i]
            total += strength[i]*(racc*(i-l) - lacc*(r-i))
        
        return total%1000000007