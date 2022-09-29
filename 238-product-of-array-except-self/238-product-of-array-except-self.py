class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [nums[0]]
        
        for i in range(1, len(nums)):
            pre.append(pre[-1]*nums[i])
        
        var = 1
        
        for i in range(len(nums)-1,-1,-1):
            if i == 0:
                pre[i] = 1*var
            else:
                pre[i] = pre[i-1]*var
                var *= nums[i]
    
        return pre