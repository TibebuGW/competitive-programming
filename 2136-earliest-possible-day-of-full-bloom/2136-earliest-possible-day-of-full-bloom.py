class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        tup=[]
        for i in range(len(plantTime)):
            tup.append([growTime[i], plantTime[i]])
            
        tup.sort(reverse = True)
        max_ = 0
        cur_time = 0
        
        for grow, plant in tup:
            cur_time += plant
            max_ = max(max_, cur_time + grow)
        return max_