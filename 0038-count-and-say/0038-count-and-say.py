class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            return self.say(self.countAndSay(n-1))
    
    def say(self, nums):
        res = []
        l = 0
        while l < len(nums):
            r = l+1
            while r < len(nums) and nums[r] == nums[l]:
                r += 1
            res.append(str(r-l))
            res.append(nums[l])
            l = r
            
        return "".join(res)