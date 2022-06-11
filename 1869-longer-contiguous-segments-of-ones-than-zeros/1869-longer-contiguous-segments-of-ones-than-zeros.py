class Solution:
    def checkZeroOnes(self, nums: str) -> bool:
        onecnt = 0
        zerocnt = 0
        oneans = 0
        zeroans = 0
        
        for num in nums:
            if num == "1":
                onecnt += 1
                oneans = max(oneans, onecnt)
            else:
                onecnt = 0
        
        for num in nums:
            if num == "0":
                zerocnt += 1
                zeroans = max(zeroans, zerocnt)
            else:
                zerocnt = 0
            
        # print(zeroans, oneans)
                
        return True if oneans > zeroans else False
        