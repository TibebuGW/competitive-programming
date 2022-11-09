class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        M = N//2
        total = sum(nums)
        if total % 2 == 1:
            return False
        half = total//2
        dp = [set() for _ in range(M+1)]
        dp[0].add(0)
        
        for num in nums:
            for i in range(len(dp)-1, 0, -1):
                for value in dp[i-1]:
                    if value+num == half:
                        return True
                    dp[i].add(value+num)
        
        return False