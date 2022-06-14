class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        new_arr = []
        popped = popped[::-1]
        i=0
        while i< len(pushed):
            new_arr.append(pushed[i])
            while len(popped)>0 and len(new_arr)>0 and new_arr[-1] == popped[-1]:
                new_arr.pop()
                popped.pop()
            i+=1
        return len(new_arr) == 0