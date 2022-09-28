class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        
        max_ = 1
        
        for i in range(len(nums)-2, -1, -1):
            temp = 1
            
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    temp = max(temp, 1+dp[j])
            dp[i] = temp
            max_ = max(max_, dp[i])
        # print(max(dp))
        return max_