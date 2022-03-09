class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        in_bound = lambda index: 0 <= index < len(flowerbed)
        # print(len(flowerbed))
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True
        
        
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if i == 0 and flowerbed[i+1] == 0:
                    count += 1
                    flowerbed[i] = 1
                elif i == len(flowerbed)-1 and flowerbed[i-1] == 0:
                    count += 1
                    flowerbed[i] = 1
                
                elif flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    count += 1
                    flowerbed[i] = 1
                    
            # print(count)
            
        if count >= n:
            return True
        
        return False