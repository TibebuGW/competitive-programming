class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [ [0] * (len(nums1)+1) for _ in range(len(nums2)+1)]
        
        for i in range(len(nums2)-1, -1, -1):
            for j in range(len(nums1)-1, -1, -1):
                if nums1[j] == nums2[i]:
                    dp[i][j] = dp[i+1][j+1] + 1
        
        return max([max(row) for row in dp])