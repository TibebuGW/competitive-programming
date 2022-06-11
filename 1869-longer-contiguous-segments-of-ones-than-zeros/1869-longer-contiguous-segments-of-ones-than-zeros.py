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
                zerocnt = 0
            else:
                zerocnt += 1
                zeroans = max(zerocnt, zeroans)
                onecnt = 0
        
        
                
        return True if oneans > zeroans else False
        